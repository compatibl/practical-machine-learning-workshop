# Copyright (C) 2021-present CompatibL
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest

from util.lag_sample import LagSample
from util.fixtures import local_test_dir


def lag_sample_test(local_test_dir) -> None:
    """
    Approval test for ShortRateTimeShiftSample.

    The test is successful if output files match git state.
    """

    # Create sample generator record
    sample = LagSample()
    sample.features = ["short_rate", "term_rate"]
    sample.lag_months = 6
    sample.countries = ["C01", "C02"]

    # Create sample
    sample.create_sample(caller_file=__file__)


if __name__ == "__main__":
    pytest.main([__file__])

