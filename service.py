import xbmc
import common as Common #from common import * #import common
## ################################################## ##
## ################################################## ##
# temp fix to stop twitter search error
import xbmcaddon

if xbmc.getCondVisibility('System.HasAddon(script.service.twitter)'):
    search_string = xbmcaddon.Addon('script.service.twitter').getSetting('search_string')
    search_string = search_string.replace('from:@','from:')
    xbmcaddon.Addon('script.service.twitter').setSetting('search_string',search_string)
    xbmcaddon.Addon('script.service.twitter').setSetting('enable_service','false')

## Start of program
TypeOfMessage="t"; (NewImage,NewMessage)=Common.FetchNews(); 
Common.CheckNews(TypeOfMessage,NewImage,NewMessage,True); 
## ################################################## ##
## ################################################## ##
