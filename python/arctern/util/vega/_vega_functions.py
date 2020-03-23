# Copyright (C) 2019-2020 Zilliz. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__all__ = [
    "vega_pointmap",
    "vega_heatmap",
    "vega_choroplethmap",
]

from arctern.util.vega.pointmap.vega_pointmap import VegaPointMap
from arctern.util.vega.heatmap.vega_heatmap import VegaHeatMap
from arctern.util.vega.choroplethmap.vega_choroplethmap import VegaChoroplethMap

def vega_pointmap(width, height,
                  bounding_box,
                  stroke_width, stroke, opacity,
                  coordinate_system="EPSG:4326"):
    return VegaPointMap(width, height,
                        bounding_box,
                        stroke_width, stroke, opacity,
                        coordinate_system)


def vega_heatmap(width, height, map_scale,
                 bounding_box,
                 coordinate_system="EPSG:4326"):
    return VegaHeatMap(width, height, map_scale,
                       bounding_box,
                       coordinate_system)

def vega_choroplethmap(width, height,
                       bounding_box,
                       color_style, ruler, opacity,
                       coordinate_system="EPSG:4326"):
    return VegaChoroplethMap(width, height,
                             bounding_box, color_style, ruler, opacity,
                             coordinate_system)
