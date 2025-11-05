# Builds tornet in array_record format
import os
import tensorflow_datasets as tfds
# from ..tornet.data.tfds.tornet import tornet_dataset_builder
import tornet.data.tfds.tornet.tornet_dataset_builder

TORNET_ROOT=os.environ['TORNET_ROOT'] # where tornet files live
TFDS_DATA_DIR=os.environ['TFDS_DATA_DIR'] # where tfds data is to be rewritten

dl_config=tfds.download.DownloadConfig(manual_dir=TORNET_ROOT)
tfds.data_source('tornet',
                data_dir=TFDS_DATA_DIR,
                builder_kwargs={'file_format':'array_record'},
                download_and_prepare_kwargs={'download_config':dl_config})
