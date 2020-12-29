from yattag import Doc, indent
from .CollectionEffort import CollectionEffort
from .MeasureCompact import MeasureCompact
from .NetInformation import NetInformation
from .SimpleContent import *

class BiologicalHabitatCollectionInformation:
  """Allows for the reporting of biological habitat sample collection information."""

  __collectionDuration: MeasureCompact
  __collectionArea: MeasureCompact
  __collectionEffort: CollectionEffort
  __reachLengthMeasure: MeasureCompact
  __reachWidthMeasure: MeasureCompact
  __collectionDescriptionText: CollectionDescriptionText
  __passCount: PassCount
  __netInformation: NetInformation

  def __init__(self, o=None, *,
    collectionDuration:MeasureCompact = None,
    collectionArea:MeasureCompact = None,
    collectionEffort:CollectionEffort = None,
    reachLengthMeasure:MeasureCompact = None,
    reachWidthMeasure:MeasureCompact = None,
    collectionDescriptionText:CollectionDescriptionText = None,
    passCount:PassCount = None,
    netInformation:NetInformation = None
  ):
    if isinstance(o, BiologicalHabitatCollectionInformation):
      # Assign attributes from objects without typechecking
      self.__collectionDuration = o.collectionDuration
      self.__collectionArea = o.collectionArea
      self.__collectionEffort = o.collectionEffort
      self.__reachLengthMeasure = o.reachLengthMeasure
      self.__reachWidthMeasure = o.reachWidthMeasure
      self.__collectionDescriptionText = o.collectionDescriptionText
      self.__passCount = o.passCount
      self.__netInformation = o.netInformation
    elif isinstance(o, dict):
      # Assign attributes from dictionary with typechecking
      self.collectionDuration = o.get('collectionDuration', default = None)
      self.collectionArea = o.get('collectionArea', default = None)
      self.collectionEffort = o.get('collectionEffort', default = None)
      self.reachLengthMeasure = o.get('reachLengthMeasure', default = None)
      self.reachWidthMeasure = o.get('reachWidthMeasure', default = None)
      self.collectionDescriptionText = o.get('collectionDescriptionText', default = None)
      self.passCount = o.get('passCount', default = None)
      self.netInformation = o.get('netInformation', default = None)
    else:
      # Assign attributes from named keywords with typechecking
      self.collectionDuration = collectionDuration
      self.collectionArea = collectionArea
      self.collectionEffort = collectionEffort
      self.reachLengthMeasure = reachLengthMeasure
      self.reachWidthMeasure = reachWidthMeasure
      self.collectionDescriptionText = collectionDescriptionText
      self.passCount = passCount
      self.netInformation = netInformation

  @property
  def collectionDuration(self) -> MeasureCompact:
    """The length of time a collection procedure or protocol was performed (e.g. total energized time for electrofishing, or total time kick net used)."""
    return self.__collectionDuration
  @collectionDuration.setter
  def collectionDuration(self, val:MeasureCompact) -> None:
    """The length of time a collection procedure or protocol was performed (e.g. total energized time for electrofishing, or total time kick net used)."""
    self.__collectionDuration = val

  @property
  def collectionArea(self) -> MeasureCompact:
    """The area of a collection procedure or protocol was performed (e.g. total area coverage for electrofishing, or total area  kick net used)."""
    return self.__collectionArea
  @collectionArea.setter
  def collectionArea(self, val:MeasureCompact) -> None:
    """The area of a collection procedure or protocol was performed (e.g. total area coverage for electrofishing, or total area  kick net used)."""
    self.__collectionArea = val

  @property
  def collectionEffort(self) -> CollectionEffort:
    return self.__collectionEffort
  @collectionEffort.setter
  def collectionEffort(self, val:CollectionEffort) -> None:
    self.__collectionEffort = val

  @property
  def reachLengthMeasure(self) -> MeasureCompact:
    """A measurement of the water body length distance in which the procedure or protocol was performed."""
    return self.__reachLengthMeasure
  @reachLengthMeasure.setter
  def reachLengthMeasure(self, val:MeasureCompact) -> None:
    """A measurement of the water body length distance in which the procedure or protocol was performed."""
    self.__reachLengthMeasure = val

  @property
  def reachWidthMeasure(self) -> MeasureCompact:
    """A measurement of the reach width during collection procedures."""
    return self.__reachWidthMeasure
  @reachWidthMeasure.setter
  def reachWidthMeasure(self, val:MeasureCompact) -> None:
    """A measurement of the reach width during collection procedures."""
    self.__reachWidthMeasure = val

  @property
  def collectionDescriptionText(self) -> CollectionDescriptionText:
    return self.__collectionDescriptionText
  @collectionDescriptionText.setter
  def collectionDescriptionText(self, val:CollectionDescriptionText) -> None:
    self.__collectionDescriptionText = None if val is None else CollectionDescriptionText(val)

  @property
  def passCount(self) -> PassCount:
    return self.__passCount
  @passCount.setter
  def passCount(self, val:PassCount) -> None:
    self.__passCount = None if val is None else PassCount(val)

  @property
  def netInformation(self) -> NetInformation:
    return self.__netInformation
  @netInformation.setter
  def netInformation(self, val:NetInformation) -> None:
    self.__netInformation = val

  def generateXML(self, name:str = 'BiologicalHabitatCollectionInformation') -> str:
    doc, tag, text, line = Doc().ttl()

    with tag(name):
      if self.__collectionDuration is not None:
        doc.asis(self.__collectionDuration.generateXML('CollectionDuration'))
      if self.__collectionArea is not None:
        doc.asis(self.__collectionArea.generateXML('CollectionArea'))
      if self.__collectionEffort is not None:
        doc.asis(self.__collectionEffort.generateXML('CollectionEffort'))
      if self.__reachLengthMeasure is not None:
        doc.asis(self.__reachLengthMeasure.generateXML('ReachLengthMeasure'))
      if self.__reachWidthMeasure is not None:
        doc.asis(self.__reachWidthMeasure.generateXML('ReachWidthMeasure'))
      if self.__collectionDescriptionText is not None:
        line('CollectionDescriptionText', self.__collectionDescriptionText)
      if self.__passCount is not None:
        line('PassCount', self.__passCount)
      if self.__netInformation is not None:
        doc.asis(self.__netInformation.generateXML('NetInformation'))

    return doc.getvalue()
