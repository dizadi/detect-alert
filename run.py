import time

from alerter import EmailAlerter
from detector_wrapper import DetectorWrapper
from dataloader import StreamLoader

class Runner:
    def __init__(
        self,
        stream_loader,
        detector_wrapper,
        alerter,
    ):
        self._detector_wrapper = detector_wrapper
        self._stream_loader = stream_loader
        self._alerter = alerter
        self._current_detections = 0

    def run(self):
        while True:
            img, img0 = next(iter(self._stream_loader))
            detections = self._detector_wrapper.detect(img)
            if len(detections) > self._current_detections:
                save_img_path = time.asctime(time.localtime())
                self._detector_wrapper.save_annotated_image(img, img0, detections)
                num_entities = len(detections)
                info = str(len(detections)) + detections[0]
                self._alerter.send_alert(
                    info,
                    save_img_path,
                )
            
            self._current_detections = len(detections)


if __name__=="__main__":
    detector_wrapper = DetectorWrapper(

    )
    stream_loader = StreamLoader(

    )
    alerter = EmailAlerter(

    )

    runner = Runner(
        stream_loader=stream_loader,
        detector_wrapper=detector_wrapper,
        alerter=alerter,
    )

    runner.run()