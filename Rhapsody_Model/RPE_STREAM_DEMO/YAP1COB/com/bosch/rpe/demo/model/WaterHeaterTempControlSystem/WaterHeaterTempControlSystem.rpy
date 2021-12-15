I-Logix-RPY-Archive version 8.14.0 C++ 9810313
{ IProject 
	- _id = GUID 7851fe6e-70b1-4e30-b83e-eb8e7c94502b;
	- _myState = 8192;
	- _properties = { IPropertyContainer 
		- Subjects = { IRPYRawContainer 
			- size = 4;
			- value = 
			{ IPropertySubject 
				- _Name = "Browser";
				- Metaclasses = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertyMetaclass 
						- _Name = "Settings";
						- Properties = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IProperty 
								- _Name = "ShowPredefinedPackage";
								- _Value = "True";
								- _Type = Bool;
							}
						}
					}
				}
			}
			{ IPropertySubject 
				- _Name = "Model";
				- Metaclasses = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertyMetaclass 
						- _Name = "Simulink";
						- Properties = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IProperty 
								- _Name = "MatlabExePath";
								- _Value = "C:\\Program Files (x86)\\MATLAB\\R2013b\\bin\\MATLAB.exe";
								- _Type = String;
							}
						}
					}
				}
			}
			{ IPropertySubject 
				- _Name = "ObjectModelGe";
				- Metaclasses = { IRPYRawContainer 
					- size = 3;
					- value = 
					{ IPropertyMetaclass 
						- _Name = "Class";
						- Properties = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IProperty 
								- _Name = "ShowPortsInterfaces";
								- _Value = "0";
								- _Type = Bool;
							}
						}
					}
					{ IPropertyMetaclass 
						- _Name = "Interface";
						- Properties = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IProperty 
								- _Name = "ShowPortsInterfaces";
								- _Value = "0";
								- _Type = Bool;
							}
						}
					}
					{ IPropertyMetaclass 
						- _Name = "Object";
						- Properties = { IRPYRawContainer 
							- size = 3;
							- value = 
							{ IProperty 
								- _Name = "ShowAttributes";
								- _Value = "None";
								- _Type = Enum;
								- _ExtraTypeInfo = "All,None,Public,Explicit";
							}
							{ IProperty 
								- _Name = "ShowOperations";
								- _Value = "All";
								- _Type = Enum;
								- _ExtraTypeInfo = "All,None,Public,Explicit";
							}
							{ IProperty 
								- _Name = "ShowPortsInterfaces";
								- _Value = "0";
								- _Type = Bool;
							}
						}
					}
				}
			}
			{ IPropertySubject 
				- _Name = "TestConductor";
				- Metaclasses = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertyMetaclass 
						- _Name = "Settings";
						- Properties = { IRPYRawContainer 
							- size = 11;
							- value = 
							{ IProperty 
								- _Name = "AcknowledgeApplyChanges";
								- _Value = "True";
								- _Type = Bool;
							}
							{ IProperty 
								- _Name = "AddQuotesToCharAndStringArguments";
								- _Value = "True";
								- _Type = Bool;
							}
							{ IProperty 
								- _Name = "CreateTestArchitectureMode";
								- _Value = "Standard";
								- _Type = Enum;
								- _ExtraTypeInfo = "Standard,Advanced";
							}
							{ IProperty 
								- _Name = "CreateTestArchitectureTransparency";
								- _Value = "BlackBox";
								- _Type = Enum;
								- _ExtraTypeInfo = "BlackBox,GreyBox";
							}
							{ IProperty 
								- _Name = "CreateTestArchitectureUsingGlobalObjects";
								- _Value = "False";
								- _Type = Bool;
							}
							{ IProperty 
								- _Name = "MapSDToTestArchitectureMode";
								- _Value = "Strict";
								- _Type = Enum;
								- _ExtraTypeInfo = "Strict,Weak";
							}
							{ IProperty 
								- _Name = "OverwriteTestContextDiagram";
								- _Value = "Never";
								- _Type = Enum;
								- _ExtraTypeInfo = "Never,Always,AskUser";
							}
							{ IProperty 
								- _Name = "ReplacementCreationMode";
								- _Value = "Wrapper";
								- _Type = Enum;
								- _ExtraTypeInfo = "Wrapper,Stub";
							}
							{ IProperty 
								- _Name = "ReportLocation";
								- _Value = "";
								- _Type = String;
							}
							{ IProperty 
								- _Name = "TestCaseExecutionOrder";
								- _Value = "BrowserOrder";
								- _Type = Enum;
								- _ExtraTypeInfo = "BrowserOrder,DeclarationOrder";
							}
							{ IProperty 
								- _Name = "TestingMode";
								- _Value = "AssertionBased";
								- _Type = Enum;
								- _ExtraTypeInfo = "AnimationBased,AssertionBased";
							}
						}
					}
				}
			}
		}
	}
	- _name = "WaterHeaterTempControlSystem";
	- Stereotypes = { IRPYRawContainer 
		- size = 1;
		- value = 
		{ IHandle 
			- _m2Class = "IStereotype";
			- _subsystem = "SysML";
			- _name = "SysML";
			- _id = GUID 052b8171-a32b-4f45-a829-5585f79f9deb;
		}
	}
	- _modifiedTimeWeak = 4.5.2021::11:47:0;
	- _description = { IDescription 
		- _text = "Tutorial starting point model version 9.";
	}
	- _lastID = 3;
	- _UserColors = { IRPYRawContainer 
		- size = 16;
		- value = 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 
	}
	- _defaultSubsystem = { ISubsystemHandle 
		- _m2Class = "ISubsystem";
		- _name = "_5_InterfacesPkg";
		- _id = GUID 6120370e-a866-4a6a-a9cf-0892e0e80fc8;
	}
	- _component = { IHandle 
		- _m2Class = "IComponent";
		- _subsystem = "TPkg_ControlSystem";
		- _name = "TPkg_ControlSystem_Comp";
		- _id = GUID a1071f62-b998-4a2f-a802-1326d3c38d0c;
	}
	- Multiplicities = { IRPYRawContainer 
		- size = 4;
		- value = 
		{ IMultiplicityItem 
			- _name = "1";
			- _count = 57;
		}
		{ IMultiplicityItem 
			- _name = "*";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "0,1";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "1..*";
			- _count = -1;
		}
	}
	- Subsystems = { IRPYRawContainer 
		- size = 14;
		- value = 
		{ IProfile 
			- fileName = "SysML";
			- _persistAs = "$OMROOT\\Profiles\\SysML\\SysMLProfile_rpy";
			- _id = GUID d9689b73-885e-44c4-896b-de43defa0a33;
			- _partOfTheModelKind = referenceunit;
		}
		{ ISubsystem 
			- fileName = "_5_InterfacesPkg";
			- _id = GUID 6120370e-a866-4a6a-a9cf-0892e0e80fc8;
		}
		{ ISubsystem 
			- fileName = "_2_ActorPkg";
			- _id = GUID 56507255-7ff1-4149-8c28-012f7aaf5685;
		}
		{ ISubsystem 
			- fileName = "_3_FunctionalAnalysisPkg";
			- _id = GUID 396bf190-9fd7-4465-919b-7b41da3e74d3;
		}
		{ ISubsystem 
			- fileName = "_4_DesignSynthesisPkg";
			- _id = GUID b4fe81a2-0e5a-4691-8eeb-8588bcbfc9e2;
		}
		{ ISubsystem 
			- fileName = "_1_RequirementsAnalysisPkg";
			- _id = GUID b5e067b9-fff8-495b-b29c-a00dbe2cef75;
		}
		{ ISubsystem 
			- fileName = "_6_TypesPkg";
			- _id = GUID d6e8afca-6e57-4d3f-a599-c2296f0f47dd;
		}
		{ IProfile 
			- fileName = "FMI";
			- _persistAs = "$OMROOT\\Profiles\\FMI";
			- _id = GUID 7c5d29e2-371f-4656-b87a-3125d68ee32a;
			- _partOfTheModelKind = referenceunit;
		}
		{ IProfile 
			- fileName = "TestingProfile";
			- _persistAs = "$OMROOT\\Profiles\\TestingProfile\\TestingProfile_rpy";
			- _id = GUID 74ef0591-fbb4-4279-a005-822d9597ffc8;
			- _partOfTheModelKind = referenceunit;
		}
		{ ISubsystem 
			- fileName = "TPkg_Sensor";
			- _id = GUID 20eab780-6390-47f1-ba60-052692c04af4;
		}
		{ IProfile 
			- fileName = "Simulink";
			- _persistAs = "$OMROOT\\Profiles\\Simulink";
			- _id = GUID a46b1a55-c20e-44bd-aed6-13d936f36a48;
			- _partOfTheModelKind = referenceunit;
		}
		{ ISubsystem 
			- fileName = "_7_TestPkg";
			- _id = GUID c7aad1c7-1c36-45a8-852f-b5c8b1123fd0;
		}
		{ ISubsystem 
			- fileName = "GatewayProjectFiles";
			- _id = GUID d9bb3551-5ab9-4586-9ffc-4a19e579bb6b;
		}
		{ ISubsystem 
			- fileName = "TPkg_ControlSystem";
			- _id = GUID 784db22d-ec3e-48e8-b9fa-acfb865094eb;
		}
	}
	- Diagrams = { IRPYRawContainer 
		- size = 0;
	}
	- Components = { IRPYRawContainer 
		- size = 0;
	}
}

