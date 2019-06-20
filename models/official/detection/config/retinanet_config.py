# Copyright 2019 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Config to train Retinanet on COCO."""

# pylint: disable=line-too-long
RETINANET_CFG = {
    'type': 'retinanet',
    'model_dir': '',
    'use_tpu': True,
    'train': {
        'iterations_per_loop': 100,
        'train_batch_size': 64,
        'total_steps': 22500,
        'optimizer': {
            'type': 'momentum',
            'momentum': 0.9,
        },
        'learning_rate': {
            'warmup_learning_rate': 0.0067,
            'warmup_steps': 500,
            'init_learning_rate': 0.08,
            'learning_rate_levels': [0.008, 0.0008],
            'learning_rate_steps': [15000, 20000],
        },
        'checkpoint': {
            'path': '',
            'prefix': '',
        },
        'variable_filter': 'resnet50_conv2',
        'train_file_pattern': '',
    },
    'eval': {
        'eval_batch_size': 8,
        'eval_samples': 5000,
        'min_eval_interval': 180,
        'eval_timeout': None,
        'num_steps_per_eval': 1000,
        'type': 'box',
        'val_json_file': '',
        'eval_file_pattern': '',
    },
    'predict': {
        'predict_batch_size': 8,
    },
    'architecture': {
        'parser': 'retinanet_parser',
        'backbone': 'resnet',
        'multilevel_features': 'fpn',
        'use_bfloat16': True,
        'l2_weight_decay': 0.0001,
    },
    'anchor': {
        'min_level': 3,
        'max_level': 7,
        'num_scales': 3,
        'aspect_ratios': [1.0, 2.0, 0.5],
        'anchor_size': 4.0,
    },
    'retinanet_parser': {
        'use_bfloat16': True,
        'output_size': [640, 640],
        'match_threshold': 0.5,
        'unmatched_threshold': 0.5,
        'aug_rand_hflip': True,
        'aug_scale_min': 1.0,
        'aug_scale_max': 1.0,
        'use_autoaugment': False,
        'autoaugment_policy_name': 'v0',
        'skip_crowd_during_training': True,
        'max_num_instances': 100,
    },
    'resnet': {
        'resnet_depth': 50,
        'dropblock_keep_prob': None,
        'dropblock_size': None,
        'batch_norm': {
            'batch_norm_momentum': 0.997,
            'batch_norm_epsilon': 1e-4,
            'batch_norm_trainable': True,
        },
    },
    'fpn': {
        'min_level': 3,
        'max_level': 7,
        'fpn_feat_dims': 256,
        'batch_norm': {
            'batch_norm_momentum': 0.997,
            'batch_norm_epsilon': 1e-4,
            'batch_norm_trainable': True,
        },
    },
    'retinanet_head': {
        'min_level': 3,
        'max_level': 7,
        'num_classes': 91,
        'anchors_per_location': 9,
        'retinanet_head_num_convs': 4,
        'retinanet_head_num_filters': 256,
        'batch_norm': {
            'batch_norm_momentum': 0.997,
            'batch_norm_epsilon': 1e-4,
            'batch_norm_trainable': True,
        },
    },
    'retinanet_loss': {
        'num_classes': 91,
        'focal_loss_alpha': 0.25,
        'focal_loss_gamma': 1.5,
        'huber_loss_delta': 0.1,
        'box_loss_weight': 50,
    },
    'postprocess': {
        'use_batched_nms': False,
        'min_level': 3,
        'max_level': 7,
        'num_classes': 91,
        'max_total_size': 100,
        'nms_iou_threshold': 0.5,
        'score_threshold': 0.05
    },
    'enable_summary': False,
}

RETINANET_RESTRICTIONS = [
    'architecture.use_bfloat16 == retinanet_parser.use_bfloat16',
    'anchor.min_level == fpn.min_level',
    'anchor.max_level == fpn.max_level',
    'anchor.min_level == retinanet_head.min_level',
    'anchor.max_level == retinanet_head.max_level',
    'anchor.min_level == postprocess.min_level',
    'anchor.max_level == postprocess.max_level',
    'retinanet_head.num_classes == retinanet_loss.num_classes',
    'retinanet_head.num_classes == postprocess.num_classes',
]

# pylint: enable=line-too-long