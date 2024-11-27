from java.lang import System
from org.json import JSONObject

System.out.println("hello java!")

jo = JSONObject("{ \"abc\" : \"def\" }")
System.out.println(jo)

# export CLASSPATH=/Users/anikrisms/Downloads/json-20140107.jar