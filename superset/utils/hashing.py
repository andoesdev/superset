# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
import hashlib
import json
import sys
from typing import Any, Dict

if sys.version_info >= (3, 9):

    def md5_sha_from_str(val: str) -> str:
        # MD5 is used to derive deterministic identifiers, not for security
        return hashlib.md5(val.encode("utf-8"), usedforsecurity=False).hexdigest()


else:

    def md5_sha_from_str(val: str) -> str:
        # MD5 is used to derive deterministic identifiers, not for security
        return hashlib.md5(val.encode("utf-8")).hexdigest()  # nosec: B324


def md5_sha_from_dict(opts: Dict[Any, Any]) -> str:
    json_data = json.dumps(opts, sort_keys=True)
    return md5_sha_from_str(json_data)
