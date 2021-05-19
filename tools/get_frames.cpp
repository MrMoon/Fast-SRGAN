#include <vector>
#include "opencv2/core.hpp"
#include "opencv2/video.hpp"
#include "opencv2/imgproc.hpp"
#include "opencv2/videoio.hpp"
#include "opencv2/highgui.hpp"

void extract_frames(const string& videoFilePath , const vector<Mat>& frames) {
	try {
		VideoCapture cap(videoFilePath);
		if(cap.isOpened() ^ 1) 
			CV_ERROR(CV_StsError , "Can not open Video File, please check the path of the video or the video itself for errors");

		for(int frameNumber = 0 ; frameNumber < cap.get(CV_CAP_PROP_FRAME_COUNT) ; ++frameNumber) {
			Mat frame;
			cap >> frame;
			frames.push_back(frame);
		}
	} catch(cv::Exception& e) {
		cerr << e.msg << '\n';
		exit(1);
	}
}

void save_frames(const string& outputDirectory , vector<Mat>& frames) {
	vector<int> compression_params;
	compression_params.push_back(CV_IMWRITE_JPEG_QUALITY);
	compression_params.push_back(100);
	long long frameNumber = 0;
	string filePath = '';
	for(std::vector<Mat>::iterator frame = frames.begin() ; frame != frames.end() ; ++frame , ++frameNumber) {
		filePath = outputDirectory + to_string(static_cast<long long>(frameNumber)) + ".jpg";
		imwrite(filePath , *frame , compression_params);
	}
}

int main() {
	vector<Mat> frames;
	const string VIDEO_PATH = "temp/video.mp4";
	const string FRAMES_PATH = "temp/video";
	extract_frames(VIDEO_PATH , frames);
	save_frames(FRAMES_PATH , frames);
	return 0;
}

