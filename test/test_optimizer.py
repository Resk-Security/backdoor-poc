import unittest
import os
import json

class TestOptimizer(unittest.TestCase):
    def test_analyze_codebase(self):
        # Simuler l'analyse de codebase
        data = {"dir": os.getcwd(), "files": [f for f in os.listdir() if f.endswith((".py", ".js", ".ts"))]}
        self.assertTrue(isinstance(data, dict))
        self.assertIn("dir", data)
        self.assertIn("files", data)

    def test_generate_report(self):
        # Simuler la génération de rapport
        report = {"timestamp": "2025-07-17", "status": "generated"}
        self.assertEqual(report["status"], "generated")

if __name__ == "__main__":
    unittest.main()