"""Define constants for OCPP integration."""
import homeassistant.components.input_number as input_number
import homeassistant.const as ha

from ocpp.v16.enums import Measurand, UnitOfMeasure

CONF_CPI = "charge_point_identity"
CONF_CPID = "cpid"
CONF_CSID = "csid"
CONF_HOST = ha.CONF_HOST
CONF_ICON = ha.CONF_ICON
CONF_IDLE_INTERVAL = "idle_interval"
CONF_MAX_CURRENT = "max_current"
CONF_METER_INTERVAL = "meter_interval"
CONF_MODE = ha.CONF_MODE
CONF_MONITORED_VARIABLES = ha.CONF_MONITORED_VARIABLES
CONF_NAME = ha.CONF_NAME
CONF_PASSWORD = ha.CONF_PASSWORD
CONF_PORT = ha.CONF_PORT
CONF_SKIP_SCHEMA_VALIDATION = "skip_schema_validation"
CONF_STEP = input_number.CONF_STEP
CONF_SUBPROTOCOL = "subprotocol"
CONF_UNIT_OF_MEASUREMENT = ha.CONF_UNIT_OF_MEASUREMENT
CONF_USERNAME = ha.CONF_USERNAME
CONF_WEBSOCKET_CLOSE_TIMEOUT = "websocket_close_timeout"
CONF_WEBSOCKET_PING_TRIES = "WEBSOCKET_PING_TRIES"
CONF_WEBSOCKET_PING_INTERVAL = "websocket_ping_interval"
CONF_WEBSOCKET_PING_TIMEOUT = "websocket_ping_timeout"
DATA_UPDATED = "ocpp_data_updated"
DEFAULT_CSID = "central"
DEFAULT_CPID = "charger"
DEFAULT_HOST = "0.0.0.0"
DEFAULT_MAX_CURRENT = 32
DEFAULT_PORT = 9000
DEFAULT_SKIP_SCHEMA_VALIDATION = False
DEFAULT_SUBPROTOCOL = "ocpp1.6"
DEFAULT_METER_INTERVAL = 60
DEFAULT_IDLE_INTERVAL = 900
DEFAULT_WEBSOCKET_CLOSE_TIMEOUT = 10
DEFAULT_WEBSOCKET_PING_TRIES = 2
DEFAULT_WEBSOCKET_PING_INTERVAL = 20
DEFAULT_WEBSOCKET_PING_TIMEOUT = 20
DOMAIN = "ocpp"
ICON = "mdi:ev-station"
SLEEP_TIME = 60

# Platforms
NUMBER = "number"
SENSOR = "sensor"
SWITCH = "switch"
BUTTON = "button"

PLATFORMS = [SENSOR, SWITCH, NUMBER, BUTTON]

# Ocpp supported measurands
MEASURANDS = [
    Measurand.energy_active_import_register.value,
    Measurand.energy_reactive_import_register.value,
    Measurand.energy_active_import_interval.value,
    Measurand.energy_reactive_import_interval.value,
    Measurand.power_active_import.value,
    Measurand.power_reactive_import.value,
    Measurand.power_offered.value,
    Measurand.power_factor.value,
    Measurand.current_import.value,
    Measurand.current_offered.value,
    Measurand.voltage.value,
    Measurand.frequency.value,
    Measurand.rpm.value,
    Measurand.soc.value,
    Measurand.temperature.value,
    Measurand.current_export.value,
    Measurand.energy_active_export_register.value,
    Measurand.energy_reactive_export_register.value,
    Measurand.energy_active_export_interval.value,
    Measurand.energy_reactive_export_interval.value,
    Measurand.power_active_export.value,
    Measurand.power_reactive_export.value,
]
DEFAULT_MEASURAND = Measurand.energy_active_import_register.value
DEFAULT_MONITORED_VARIABLES = ",".join(MEASURANDS)
DEFAULT_ENERGY_UNIT = UnitOfMeasure.wh.value
DEFAULT_POWER_UNIT = UnitOfMeasure.w.value
HA_ENERGY_UNIT = UnitOfMeasure.kwh.value
HA_POWER_UNIT = UnitOfMeasure.kw.value

# Where a HA unit does not exist use Ocpp unit
UNITS_OCCP_TO_HA = {
    UnitOfMeasure.wh: ha.ENERGY_WATT_HOUR,
    UnitOfMeasure.kwh: ha.ENERGY_KILO_WATT_HOUR,
    UnitOfMeasure.varh: UnitOfMeasure.varh,
    UnitOfMeasure.kvarh: UnitOfMeasure.kvarh,
    UnitOfMeasure.w: ha.POWER_WATT,
    UnitOfMeasure.kw: ha.POWER_KILO_WATT,
    UnitOfMeasure.va: ha.POWER_VOLT_AMPERE,
    UnitOfMeasure.kva: UnitOfMeasure.kva,
    UnitOfMeasure.var: UnitOfMeasure.var,
    UnitOfMeasure.kvar: UnitOfMeasure.kvar,
    UnitOfMeasure.a: ha.ELECTRIC_CURRENT_AMPERE,
    UnitOfMeasure.v: ha.ELECTRIC_POTENTIAL_VOLT,
    UnitOfMeasure.celsius: ha.TEMP_CELSIUS,
    UnitOfMeasure.fahrenheit: ha.TEMP_FAHRENHEIT,
    UnitOfMeasure.k: ha.TEMP_KELVIN,
    UnitOfMeasure.percent: ha.PERCENTAGE,
    UnitOfMeasure.hertz: ha.FREQUENCY_HERTZ,
}
