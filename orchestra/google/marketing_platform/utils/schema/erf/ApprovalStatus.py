###########################################################################
#
#  Copyright 2017 Google Inc.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
###########################################################################

ApprovalStatus_Schema = [
  { "name":"auditor",
    "type":"INTEGER",
    "mode":"NULLABLE",
  },
  { "name":"status",
    "type":"INTEGER",
    "mode":"NULLABLE",
  },
  { "name":"feedback",
    "type":"STRING",
    "mode":"NULLABLE",
  },
  { "name":"sync_time",
    "type":"INTEGER",
    "mode":"NULLABLE",
  },
  { "name":"external_id",
    "type":"INTEGER",
    "mode":"NULLABLE",
  },
]