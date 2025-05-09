from typing import cast

from app.system.constants import MAIL, PASS
from app.system.manager import Manager


# New Approved Committed External Test Accepted Review Done

checks = 'Accepted'

Manager.run_pipeline(cast(str, MAIL), cast(str, PASS), checks)
