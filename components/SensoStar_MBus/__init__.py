import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import uart
from esphome.const import CONF_ID

DEPENDENCIES = ["uart"]

CONF_SENSOSTAR_ID = "sensostar_id"

sensostar = cg.esphome_ns.namespace("sensostar")
SensoStarComponent = sensostar.class_(
    "SensoStarComponent", cg.PollingComponent, uart.UARTDevice
)

CONFIG_SCHEMA = (
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(SensoStarComponent)
        }
    )
    .extend(uart.UART_DEVICE_SCHEMA)
    .extend(cv.polling_component_schema("30s"))
)

FINAL_VALIDATE_SCHEMA = uart.final_validate_device_schema(
    "SensoStar_MBus",
    require_tx=True,
    require_rx=True,
    baud_rate=2400,
    parity="EVEN",
    stop_bits=1,
)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await uart.register_uart_device(var, config)