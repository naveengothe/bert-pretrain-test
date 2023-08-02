#!/Users/gothena/opt/anaconda3/bin/python
# Copyright 2022 VMware, Inc.
# SPDX-License-Identifier: Apache-2.0

from setuptools import setup

setup(
    name='bert_pretrain',
    version='0.1.0',
    description='Bert Pretraining on custom data',
    author='Naveen Gothe',
    license='Apache-2.0',
    python_requires='>=3.7',
    packages=['bert_pretrain'],

    install_requires=['numpy',
                      'scikit-learn',
                      'pandas',
                      'protobuf~=3.19.0',
                      'torch==1.13.1',
                      'accelerate~=0.6.0',
                      'transformers~=4.18.0',
                      'tfrecord>=1.14.1'
                      ]
)