#
# Short filter module to expand a string of vlans into an unordered list
# Input example string, as per Cisco IOS cli scrape:  "10,20,23,27-30,41"
# Output example list expanded = [10, 20, 23, 27, 28, 29, 30, 41]
#

from jinja2 import TemplateError

class FilterModule(object):

    def expand_vlans(self,vlanList,*argv):
 #       print vlanList
 #       if type(vlanList) is not str:
 #           raise TemplateError("First argument must be string of vlans")
    
        expanded = []
        splitList = vlanList.split(",")
      
        for item in splitList:
            if "-" in item:
                chunk = item.split("-")
                for vlan in range(int(chunk[0]), int(chunk[1]) + 1):
                    expanded.append(vlan)
            else:
                expanded.append(int(item))
    
        return expanded
    
    def filters(self):
        return {
          'expand_vlans'  : self.expand_vlans
        }
            