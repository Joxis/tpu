export PYTHONPATH=$PYTHONPATH:./models:./models/official/efficientnet
MODEL="segmentation"
EXPORT_DIR="output"
CHECKPOINT_PATH="weights/efficientnet-b7-nasfpn-ssl/model.ckpt"
CONFIG_PATH="configs/pascal_seg_efficientnet-b7-nasfpn.yaml"
PARAMS_OVERRIDE=""  # if any.
BATCH_SIZE=1
INPUT_TYPE="image_bytes"
INPUT_NAME="input"
INPUT_IMAGE_SIZE="512,512"
python models/official/detection/export_saved_model.py \
  --export_dir="${EXPORT_DIR?}" \
  --checkpoint_path="${CHECKPOINT_PATH?}" \
  --params_override="${PARAMS_OVERRIDE?}" \
  --batch_size=${BATCH_SIZE?} \
  --input_type="${INPUT_TYPE?}" \
  --input_name="${INPUT_NAME?}" \
  --input_image_size="${INPUT_IMAGE_SIZE?}" \
  --model="${MODEL?}" \
  --config_file="${CONFIG_PATH?}" \
