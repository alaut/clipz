import yaml
from datetime import datetime
import os

def clipz(input_file, test=True, output_folder = '.\\'):
    print('Loading {}...'.format(input_file))
    with open(input_file) as f:
        clips = yaml.load(f, Loader=yaml.FullLoader)

    for clip in clips:
        input_video = list(clip.keys())[0]

        try:
            os.mkdir(output_folder)
        except:
            pass

        for start, stop, output_video in clip[input_video]:
            print('{}-{}\t{}'.format(start, stop, output_video))
  
            delta = datetime.strptime(stop, '%M:%S') - datetime.strptime(start, '%M:%S')
            input_path = os.path.abspath(input_video)
            output_path = os.path.abspath(output_folder +'\\' + output_video)

            cmd = 'ffmpeg -i "{:}" -ss {:} -t {:} "{:}"'.format(input_path, start, str(delta), output_path)
            
            if test:
                print(cmd)
            else:
                os.system(cmd)