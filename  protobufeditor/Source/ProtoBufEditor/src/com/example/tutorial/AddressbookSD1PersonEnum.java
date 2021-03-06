// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: addressbookSD1_PersonEnum.proto

package com.example.tutorial;

public final class AddressbookSD1PersonEnum {
  private AddressbookSD1PersonEnum() {}
  public static void registerAllExtensions(
      com.google.protobuf.ExtensionRegistry registry) {
  }
  public enum PhoneType
      implements com.google.protobuf.ProtocolMessageEnum {
    MOBILE(0, 0),
    HOME(1, 1),
    WORK(2, 2),
    ;
    
    public static final int MOBILE_VALUE = 0;
    public static final int HOME_VALUE = 1;
    public static final int WORK_VALUE = 2;
    
    
    public final int getNumber() { return value; }
    
    public static PhoneType valueOf(int value) {
      switch (value) {
        case 0: return MOBILE;
        case 1: return HOME;
        case 2: return WORK;
        default: return null;
      }
    }
    
    public static com.google.protobuf.Internal.EnumLiteMap<PhoneType>
        internalGetValueMap() {
      return internalValueMap;
    }
    private static com.google.protobuf.Internal.EnumLiteMap<PhoneType>
        internalValueMap =
          new com.google.protobuf.Internal.EnumLiteMap<PhoneType>() {
            public PhoneType findValueByNumber(int number) {
              return PhoneType.valueOf(number);
            }
          };
    
    public final com.google.protobuf.Descriptors.EnumValueDescriptor
        getValueDescriptor() {
      return getDescriptor().getValues().get(index);
    }
    public final com.google.protobuf.Descriptors.EnumDescriptor
        getDescriptorForType() {
      return getDescriptor();
    }
    public static final com.google.protobuf.Descriptors.EnumDescriptor
        getDescriptor() {
      return com.example.tutorial.AddressbookSD1PersonEnum.getDescriptor().getEnumTypes().get(0);
    }
    
    private static final PhoneType[] VALUES = {
      MOBILE, HOME, WORK, 
    };
    
    public static PhoneType valueOf(
        com.google.protobuf.Descriptors.EnumValueDescriptor desc) {
      if (desc.getType() != getDescriptor()) {
        throw new java.lang.IllegalArgumentException(
          "EnumValueDescriptor is not for this type.");
      }
      return VALUES[desc.getIndex()];
    }
    
    private final int index;
    private final int value;
    
    private PhoneType(int index, int value) {
      this.index = index;
      this.value = value;
    }
    
    // @@protoc_insertion_point(enum_scope:PhoneType)
  }
  
  
  public static com.google.protobuf.Descriptors.FileDescriptor
      getDescriptor() {
    return descriptor;
  }
  private static com.google.protobuf.Descriptors.FileDescriptor
      descriptor;
  static {
    java.lang.String[] descriptorData = {
      "\n\037addressbookSD1_PersonEnum.proto*+\n\tPho" +
      "neType\022\n\n\006MOBILE\020\000\022\010\n\004HOME\020\001\022\010\n\004WORK\020\002B\026" +
      "\n\024com.example.tutorial"
    };
    com.google.protobuf.Descriptors.FileDescriptor.InternalDescriptorAssigner assigner =
      new com.google.protobuf.Descriptors.FileDescriptor.InternalDescriptorAssigner() {
        public com.google.protobuf.ExtensionRegistry assignDescriptors(
            com.google.protobuf.Descriptors.FileDescriptor root) {
          descriptor = root;
          return null;
        }
      };
    com.google.protobuf.Descriptors.FileDescriptor
      .internalBuildGeneratedFileFrom(descriptorData,
        new com.google.protobuf.Descriptors.FileDescriptor[] {
        }, assigner);
  }
  
  // @@protoc_insertion_point(outer_class_scope)
}
