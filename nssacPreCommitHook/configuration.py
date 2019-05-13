import json
import sys
from jsonschema import validate

class Configuration:
    
    def __init__(self):
        self.schema = {
              "$schema": "http://json-schema.org/draft-07/schema#",
              "title": "Schema title",
              "description": "Description of the schema",
              "definitions": {
                "gitWildMatchPattern": {
                  "description": "A string int used for pattern matching as used in .gitattributes",
                  "type": "string"
                },
                "regexp": {
                  "description": "A python regular expression",
                  "type": "string"
                },
                "multiLineText": {
                  "type": "array",
                  "items": {"type": "string"},
                  "minItems": 1
                }
              },
              "type": "object",
              "required": [
                "copyright",
                "patterns"
              ],
              "properties": {
                "license": {
                  "description": "Text referring to the license applied to the file",
                  "$ref": "#/definitions/multiLineText"
                },
                "copyright": {
                  "description": "A list of copyright statements optionally the including the range of years it was valid. The place holder %s will be replaced with the year range",
                  "type": "array",
                  "items": {
                    "type": "object",
                    "required": ["text"],
                    "properties": {
                      "text": {"$ref": "#/definitions/multiLineText"},
                      "startYear": {"type": "number"}
                    },
                    "additionalProperties": False
                  },
                  "minItems": 1
                },
                "patterns": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "required": [
                      "include",
                      "commentStart"
                    ],
                    "properties": {
                      "include": {
                        "type": "array",
                        "items": {"$ref": "#/definitions/gitWildMatchPattern"},
                        "minItems": 1
                      },
                      "exclude": {
                        "type": "array",
                        "items": {"$ref": "#/definitions/gitWildMatchPattern"}
                      },
                      "commentStart": {"type": "string"},
                      "commentEnd": {"type": "string"},
                      "prolog": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "required": ["end"],
                          "properties": {
                            "end": {"$ref": "#/definitions/regexp"},
                            "maxLines": {"type": "number"}
                          },
                          "additionalProperties": False
                        }
                      }
                    },
                    "additionalProperties": False
                  },
                  "minItems": 1
                }
              },
              "patternProperties": {
                "^\\$": {}
              }, 
              "additionalProperties": False
            }
        return
        
    def loadJsonFile(self, fileName, jsonSchema = None):
    
        try:
            jsonFile = open(fileName,"r")
        
        except:
            sys.exit("ERROR: File '" + fileName + "' does not exist.")
        
        dictionary = json.load(jsonFile)
        
        if jsonSchema != None:
            try:
                schemaFile = open(jsonSchema,"r")
        
            except:
                sys.exit("ERROR: File '" + schemaFile + "' does not exist.")
                    
            schema = json.load(schemaFile)
            schemaFile.close()
        else:
            schema = self.schema
            
        validate(dictionary, schema)
            
        jsonFile.close()
        return dictionary
