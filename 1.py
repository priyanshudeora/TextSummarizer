from src.textSummarizer.config.configuration import ConfigurationManager
config = ConfigurationManager()
print(config.config.data_transformation)  # This should work without error
