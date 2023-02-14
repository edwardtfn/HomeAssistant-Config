"""TS011F plug."""

from zigpy.profiles import zha
from zigpy.quirks import CustomDevice
from zigpy.zcl.clusters.general import (
    Basic,
    GreenPowerProxy,
    Groups,
    Identify,
    OnOff,
    Ota,
    Scenes,
    Time,
)
from zigpy.zcl.clusters.homeautomation import ElectricalMeasurement
from zigpy.zcl.clusters.smartenergy import Metering

from zhaquirks.const import (
    DEVICE_TYPE,
    ENDPOINTS,
    INPUT_CLUSTERS,
    MODEL,
    MODELS_INFO,
    OUTPUT_CLUSTERS,
    PROFILE_ID,
)
from zhaquirks.tuya import (
    TuyaNewManufCluster,
    TuyaZBE000Cluster,
    TuyaZBElectricalMeasurement,
    TuyaZBExternalSwitchTypeCluster,
    TuyaZBMeteringCluster,
    TuyaZBOnOffAttributeCluster,
)
from zhaquirks.tuya.mcu import EnchantedDevice


class Plug_4AC_2USB_cfnprab5(EnchantedDevice):
    """Tuya 4 outlet + 2 USB surge protector with restore power state support."""

    signature = {
        MODEL: "TS011F",
        ENDPOINTS: {
            # <SimpleDescriptor endpoint=1 profile=260 device_type=266
            # device_version=1
            # input_clusters=[0, 3, 4, 5, 6, 57344, 57345]
            # output_clusters=[10, 25]>
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_PLUG_IN_UNIT,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    OnOff.cluster_id,
                    TuyaZBE000Cluster.cluster_id,
                    TuyaZBExternalSwitchTypeCluster.cluster_id,
                ],
                OUTPUT_CLUSTERS: [Time.cluster_id, Ota.cluster_id],
            },
            # <SimpleDescriptor endpoint=2 profile=260 device_type=266
            # device_version=1
            # input_clusters=[4, 5, 6, 57345]
            # output_clusters=[]>
            2: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_PLUG_IN_UNIT,
                INPUT_CLUSTERS: [
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    OnOff.cluster_id,
                    TuyaZBExternalSwitchTypeCluster.cluster_id,
                ],
                OUTPUT_CLUSTERS: [],
            },
            # <SimpleDescriptor endpoint=3 profile=260 device_type=266
            # device_version=1
            # input_clusters=[4, 5, 6, 57345]
            # output_clusters=[]>
            3: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_PLUG_IN_UNIT,
                INPUT_CLUSTERS: [
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    OnOff.cluster_id,
                    TuyaZBExternalSwitchTypeCluster.cluster_id,
                ],
                OUTPUT_CLUSTERS: [],
            },
            # <SimpleDescriptor endpoint=4 profile=260 device_type=266
            # device_version=1
            # input_clusters=[4, 5, 6, 57345]
            # output_clusters=[]>
            4: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_PLUG_IN_UNIT,
                INPUT_CLUSTERS: [
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    OnOff.cluster_id,
                    TuyaZBExternalSwitchTypeCluster.cluster_id,
                ],
                OUTPUT_CLUSTERS: [],
            },
            # <SimpleDescriptor endpoint=5 profile=260 device_type=266
            # device_version=1
            # input_clusters=[4, 5, 6, 57345]
            # output_clusters=[]>
            5: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_PLUG_IN_UNIT,
                INPUT_CLUSTERS: [
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    OnOff.cluster_id,
                    TuyaZBExternalSwitchTypeCluster.cluster_id,
                ],
                OUTPUT_CLUSTERS: [],
            },
            # <SimpleDescriptor endpoint=242 profile=41440 device_type=97
            # device_version=1
            # input_clusters=[]
            # output_clusters=[33]>
            242: {
                PROFILE_ID: 41440,
                DEVICE_TYPE: 97,
                INPUT_CLUSTERS: [],
                OUTPUT_CLUSTERS: [GreenPowerProxy.cluster_id],
            },
        },
    }
    replacement = {
        ENDPOINTS: {
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_PLUG_IN_UNIT,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    TuyaZBOnOffAttributeCluster,
                    TuyaZBE000Cluster,
                    TuyaZBExternalSwitchTypeCluster,
                ],
                OUTPUT_CLUSTERS: [Time.cluster_id, Ota.cluster_id],
            },
            2: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_PLUG_IN_UNIT,
                INPUT_CLUSTERS: [
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    TuyaZBOnOffAttributeCluster,
                    TuyaZBExternalSwitchTypeCluster,
                ],
                OUTPUT_CLUSTERS: [],
            },
            3: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_PLUG_IN_UNIT,
                INPUT_CLUSTERS: [
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    TuyaZBOnOffAttributeCluster,
                    TuyaZBExternalSwitchTypeCluster,
                ],
                OUTPUT_CLUSTERS: [],
            },
            4: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_PLUG_IN_UNIT,
                INPUT_CLUSTERS: [
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    TuyaZBOnOffAttributeCluster,
                    TuyaZBExternalSwitchTypeCluster,
                ],
                OUTPUT_CLUSTERS: [],
            },
            5: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_PLUG_IN_UNIT,
                INPUT_CLUSTERS: [
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    TuyaZBOnOffAttributeCluster,
                    TuyaZBExternalSwitchTypeCluster,
                ],
                OUTPUT_CLUSTERS: [],
            },
            242: {
                PROFILE_ID: 41440,
                DEVICE_TYPE: 97,
                INPUT_CLUSTERS: [],
                OUTPUT_CLUSTERS: [GreenPowerProxy.cluster_id],
            },
        },
    }

class Plug_4AC_2USB_Var04(EnchantedDevice):
    """Tuya 4 outlet + 2 USB (variation 04))."""

    signature = {
        MODEL: "TS011F",
        ENDPOINTS: {
            # <SimpleDescriptor endpoint=1 profile=260 device_type=266
            # device_version=1
            # input_clusters=["0x0000","0x0003","0x0004","0x0005","0x0006","0xe001"]
            # output_clusters=[]>
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    OnOff.cluster_id,
                    TuyaZBExternalSwitchTypeCluster.cluster_id,
                ],
                OUTPUT_CLUSTERS: [],
            },
            2: {
                # input_clusters=["0x0000","0x0003","0x0004","0x0005","0x0006","0xe001"]
                # output_clusters=[]
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    OnOff.cluster_id,
                    TuyaZBExternalSwitchTypeCluster.cluster_id,
                ],
                OUTPUT_CLUSTERS: [],
            },
            3: {
                # input_clusters=["0x0000","0x0003","0x0004","0x0005","0x0006","0xe001"]
                # output_clusters=[]
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    OnOff.cluster_id,
                    TuyaZBExternalSwitchTypeCluster.cluster_id,
                ],
                OUTPUT_CLUSTERS: [],
            },
            4: {
                # input_clusters=["0x0000","0x0003","0x0004","0x0005","0x0006","0xe001"]
                # output_clusters=[]
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    OnOff.cluster_id,
                    TuyaZBExternalSwitchTypeCluster.cluster_id,
                ],
                OUTPUT_CLUSTERS: [],
            },
            5: {
                # input_clusters=["0x0000","0x0003","0x0004","0x0005","0x0006","0xe001"]
                # output_clusters=[]
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    OnOff.cluster_id,
                    TuyaZBExternalSwitchTypeCluster.cluster_id,
                ],
                OUTPUT_CLUSTERS: [],
            },
        },
    }
    replacement = {
        ENDPOINTS: {
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_PLUG_IN_UNIT,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    TuyaZBOnOffAttributeCluster,
                    TuyaZBExternalSwitchTypeCluster,
                ],
                OUTPUT_CLUSTERS: [],
            },
            2: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_PLUG_IN_UNIT,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    TuyaZBOnOffAttributeCluster,
                    TuyaZBExternalSwitchTypeCluster,
                ],
                OUTPUT_CLUSTERS: [],
            },
            3: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_PLUG_IN_UNIT,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    TuyaZBOnOffAttributeCluster,
                    TuyaZBExternalSwitchTypeCluster,
                ],
                OUTPUT_CLUSTERS: [],
            },
            4: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_PLUG_IN_UNIT,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    TuyaZBOnOffAttributeCluster,
                    TuyaZBExternalSwitchTypeCluster,
                ],
                OUTPUT_CLUSTERS: [],
            },
            5: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_PLUG_IN_UNIT,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    TuyaZBOnOffAttributeCluster,
                    TuyaZBExternalSwitchTypeCluster,
                ],
                OUTPUT_CLUSTERS: [],
            },
        },
    }
