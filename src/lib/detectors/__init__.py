from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from .exdet import ExdetDetector
from .ddd import DddDetector
from .ctdet import CtdetDetector
from .multi_pose import MultiPoseDetector

_detector_factory = {
    'exdet': ExdetDetector,
    'ddd': DddDetector,
    'ctdet': CtdetDetector,
    'multi_pose': MultiPoseDetector,
}

def build_detector(task):
    return _detector_factory[task]
