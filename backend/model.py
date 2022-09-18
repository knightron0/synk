import deepspeech

model_file_path = '/Users/sarthakmangla/code/deepspeech-0.9.3-models.pbmm'
beam_width = 500
model = deepspeech.Model(model_file_path, beam_width)

