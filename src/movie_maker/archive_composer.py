import moviepy.editor as mp
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.compositing.concatenate import concatenate_videoclips
from moviepy.video.io.VideoFileClip import VideoFileClip


class Compositor:
    def __init__(self, clip, intro='../../media/archiwum_intro.mp4', alg='bicubic', size=None, oberver=None):
        intro_clip = VideoFileClip(intro).set_position(('center', 'center'))
        archive_clip = mp.VideoFileClip(clip, resize_algorithm=alg)
        if size is None:
            width = max([intro_clip.size[0], archive_clip.size[0]])
            height = max([intro_clip.size[1], archive_clip.size[1]])
            size = (width, height)
        archive_clip = archive_clip.resize(size)

        self.final_clip = concatenate_videoclips([intro_clip, archive_clip])
        self.final_clip = CompositeVideoClip([self.final_clip])

    def write(self, clip_name, logger='bar'):
        self.final_clip.write_videofile(clip_name, logger=logger)
