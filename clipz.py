import csv
import os
from datetime import datetime
from subprocess import call
from pathlib import Path

# import datetime
import yaml


def clipz(input_file, check=True):
    print('Loading {}...'.format(input_file))
    with open(input_file) as f:
        clips = yaml.load(f, Loader=yaml.FullLoader)

    for clip in clips:
        input_video = list(clip.keys())[0]
        # print(input_video)

        for start, stop, output_video in clip[input_video]:
            # print('{}-{}\t{}'.format(start, stop, output_video))
            fmt = '%M:%S'
            delta = datetime.strptime(stop, fmt) - datetime.strptime(start, fmt)

            input_path = os.path.abspath(input_video)
            output_path = os.path.abspath(output_video)

            cmd = 'ffmpeg -i "{:}" -ss {:} -t {:} "{:}"'.format(input_path, start, str(delta), output_path)


            # cmd = 'ffmpeg -i "'+fin+'" -ss '+t0+' -t '+dt+' "'+fout+'"'
            print(cmd)
            if not(check):
                # os.system(cmd)
                pass


if __name__=="__main__":
    clipz('.\example.yaml')