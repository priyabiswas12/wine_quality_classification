from src.wine_quality_classification import logger
from wine_quality_classification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
#from wine_quality_classificationpipeline.stage_02_data_validation import DataValidationTrainingPipeline
#from wine_quality_classification.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
#from wine_quality_classification.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
#from wine_quality_classification.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline


STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
