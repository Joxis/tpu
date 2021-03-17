export PYTHONPATH=$PYTHONPATH:./models:./models/official/efficientnet
MODEL="segmentation"
IMAGE_SIZE=640
CHECKPOINT_PATH="weights/efficientnet-b7-nasfpn-ssl/model.ckpt"
CONFIG_PATH="configs/pascal_seg_efficientnet-b7-nasfpn.yaml"
LABEL_MAP_FILE="./models/official/detection/datasets/coco_label_map.csv"
IMAGE_FILE_PATTERN="data/images/*.jpg"
OUTPUT_HTML="./test.html"
python models/official/detection/inference.py \
  --model="${MODEL?}" \
  --image_size=${IMAGE_SIZE?} \
  --checkpoint_path="${CHECKPOINT_PATH?}" \
  --label_map_file="${LABEL_MAP_FILE?}" \
  --image_file_pattern="${IMAGE_FILE_PATTERN?}" \
  --output_html="${OUTPUT_HTML?}" \
  --max_boxes_to_draw=10 \
  --min_score_threshold=0.05 \
  --config_file="${CONFIG_PATH?}"