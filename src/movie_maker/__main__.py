import argparse

from src.movie_maker.archive_composer import Compositor

parser = argparse.ArgumentParser(
    description='Pass the video clip path to add intro_clip before. Output video clip is genereted in place'
                + 'Output video is concatenated and resize to greates resulution of input videos.')
parser.add_argument('input_video_clip', type=str, nargs='+', help='input video file path')
parser.add_argument('--intro', type=str, nargs='?', help='input video file path')
parser.add_argument('-w', '--width', type=int, nargs=1, help='width of output video file')
parser.add_argument('-h', '--height', type=int, nargs=1, help='height output video file')
parser.add_argument('--alg', type=str, nargs=1, help='resize algorythm can be one of: fast_bilinear ' +
                                                     'bilinear, bicubic, experimental, neighbor, area, bicublin, '
                                                     'gauss, sinc, lanczos, spline, print_info, accurate_rnd, '
                                                     'full_chroma_int, full_chroma_inp, bitexact')

args = parser.parse_args()

intro = 'media/archiwum_intro.mp4' if not args.intro else args.intro
size = (args.width, args.height)
actual_video_clip = args.input_video_clip
alg = args.alg

compositor = Compositor(intro, actual_video_clip, alg, size)
compositor.write(f'#Archiwum - {actual_video_clip}' + '.mp4')
