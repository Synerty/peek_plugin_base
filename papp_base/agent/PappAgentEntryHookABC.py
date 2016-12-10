from typing import Optional

from papp_base.PappCommonEntryHookABC import PappCommonEntryHookABC
from papp_base.worker.PeekWorkerPlatformABC import PeekWorkerPlatformABC


class PappAgentEntryHookABC(PappCommonEntryHookABC):

    def __init__(self, pappName: str, pappRootDir: str, platform: PeekWorkerPlatformABC):
        PappCommonEntryHookABC.__init__(self, pappName=pappName, pappRootDir=pappRootDir)
        self._platform = platform

    @property
    def publishedAgentApi(self, requestingPappName:str) -> Optional[object]:
        return None
