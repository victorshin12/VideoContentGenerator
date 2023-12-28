from moviepy.editor import VideoFileClip, clips_array

def process_video(video_path, start_time, end_time, target_width):
    # Load video clip
    clip = VideoFileClip(video_path).subclip(start_time, end_time)

    # Calculate target height based on the desired aspect ratio (1080 x 1920)
    aspect_ratio = 1080 / 1920
    target_height = int(target_width / aspect_ratio)

    # Resize while maintaining aspect ratio
    clip_resized = clip.resize(width=target_width, height=target_height)

    # Calculate cropping box
    center_x, center_y = clip_resized.size[0] // 2, clip_resized.size[1] // 2
    crop_x1 = center_x - target_width
    crop_y1 = center_y - target_height // 2
    crop_x2 = center_x + target_width
    crop_y2 = center_y + target_height // 2

    # Crop the video
    clip_cropped = clip_resized.crop(x1=crop_x1, y1=crop_y1, x2=crop_x2, y2=crop_y2)

    return clip_cropped

def main():
    # Replace these paths with the actual paths to your videos
    video1_path = 'dailydose.mp4'
    video2_path = 'gta.mp4'
    output_path = 'output.mp4'

    # Set parameters
    target_width = 1020
    frame_limit = 200

    # Process first video
    clip1 = process_video(video1_path, 0, frame_limit / 30, target_width)

    # Process second video and mute it
    clip2 = process_video(video2_path, 0, frame_limit / 30, target_width).set_audio(None)

    # Combine the two clips vertically
    final_clip = clips_array([[clip1], [clip2]])

    # Export the final video
    final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

if __name__ == "__main__":
    main()
