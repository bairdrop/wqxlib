from yattag import Doc, indent
from .SimpleContent import *
from ..common import WQXException

class ActivityGroup:
  """Allows for the grouping of activities."""

  __activityGroupIdentifier: ActivityGroupIdentifier
  __activityGroupName: ActivityGroupName
  __activityGroupTypeCode: ActivityGroupTypeCode
  __activityIdentifier: ActivityIdentifier
  __replaceActivities: bool

  def __init__(self, o=None, *,
    activityGroupIdentifier:ActivityGroupIdentifier = None,
    activityGroupName:ActivityGroupName = None,
    activityGroupTypeCode:ActivityGroupTypeCode = None,
    activityIdentifier:ActivityIdentifier = None,
    replaceActivities:bool = False
  ):
    if isinstance(o, ActivityGroup):
      # Assign attributes from object without typechecking
      self.__activityGroupIdentifier = o.activityGroupIdentifier
      self.__activityGroupName = o.activityGroupName
      self.__activityGroupTypeCode = o.activityGroupTypeCode
      self.__activityIdentifier = o.activityIdentifier
      self.__replaceActivities = o.replaceActivities
    elif isinstance(o, dict):
      # Assign attributes from dictionary with typechecking
      self.activityGroupIdentifier = o.get('activityGroupIdentifier', default = None)
      self.activityGroupName = o.get('activityGroupName', default = None)
      self.activityGroupTypeCode = o.get('activityGroupTypeCode', default = None)
      self.activityIdentifier = o.get('activityIdentifier', default = None)
      self.replaceActivities = o.get('replaceActivities', default = False)
    else:
      # Assign attributes from named keywords with typechecking
      self.activityGroupIdentifier = activityGroupIdentifier
      self.activityGroupName = activityGroupName
      self.activityGroupTypeCode = activityGroupTypeCode
      self.activityIdentifier = activityIdentifier
      self.replaceActivities = replaceActivities

  @property
  def activityGroupIdentifier(self) -> ActivityGroupIdentifier:
    return self.__activityGroupIdentifier
  @activityGroupIdentifier.setter
  def activityGroupIdentifier(self, val:ActivityGroupIdentifier) -> None:
    self.__activityGroupIdentifier = None if val is None else ActivityGroupIdentifier(val)

  @property
  def activityGroupName(self) -> ActivityGroupName:
    return self.__activityGroupName
  @activityGroupName.setter
  def activityGroupName(self, val:ActivityGroupName) -> None:
    self.__activityGroupName = None if val is None else ActivityGroupName(val)

  @property
  def activityGroupTypeCode(self) -> ActivityGroupTypeCode:
    return self.__activityGroupTypeCode
  @activityGroupTypeCode.setter
  def activityGroupTypeCode(self, val:ActivityGroupTypeCode) -> None:
    self.__activityGroupTypeCode = None if val is None else ActivityGroupTypeCode(val)

  @property
  def activityIdentifier(self) -> ActivityIdentifier:
    return self.__activityIdentifier
  @activityIdentifier.setter
  def activityIdentifier(self, val:ActivityIdentifier) -> None:
    self.__activityIdentifier = None if val is None else ActivityIdentifier(val)

  @property
  def replaceActivities(self) -> bool:
    return self.__replaceActivities
  @replaceActivities.setter
  def replaceActivities(self, val:bool) -> None:
    if not isinstance(val, bool):
      raise WQXException("Attribute 'replaceActivities' must be a boolean.")
    self.__replaceActivities = val

  def generateXML(self, name:str = 'ActivityGroup') -> str:
    doc, tag, text, line = Doc().ttl()

    with tag(name,
      ('ReplaceActivities', str(self.__replaceActivities))
    ):
      if self.__activityGroupIdentifier is None:
        raise WQXException("Attribute 'activityGroupIdentifier' is required.")
      line('ActivityGroupIdentifier', self.__activityGroupIdentifier)
      if self.__activityGroupName is not None:
        line('ActivityGroupName', self.__activityGroupName)
      if self.__activityGroupTypeCode is None:
        raise WQXException("Attribute 'activityGroupTypeCode' is required.")
      line('ActivityGroupTypeCode', self.__activityGroupTypeCode)
      if len(self.__activityIdentifier) < 2:
        raise WQXException("Attribute 'activityIdentifier' must be a list of 2 or more ActivityIdentifier objects.")
      for x in self.__activityIdentifier:
        line('ActivityIdentifier', x)

    return doc.getvalue()
