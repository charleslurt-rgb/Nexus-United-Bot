import discord
from discord import app_commands
from discord.ext import commands


# ============================================================
# SERVICE DATA
# ============================================================

SERVICES = {
    "discord_server": {
        "name": "Discord Server Creation",
        "price": "$1.50 – $10.00",
        "details": (
            "**Base Server — $1.50**\n"
            "A fully structured server tailored to your community "
            "or business niche. This includes setting up a logical "
            "channel hierarchy, configuring basic role permissions, "
            "and integrating standard moderation bots to ensure "
            "your server is secure and operational from day one.\n\n"
            "**Advanced Setup — $5.00–$10.00**\n"
            "Includes custom welcome messages and self-assignable "
            "reaction roles. The Advanced Setup contains pre-made "
            "embeds and sometimes custom bots depending on the price."
        ),
    },

    "custom_bot": {
        "name": "Custom Discord Bot",
        "price": "$2.50 – $5.00",
        "details": (
            "A dedicated, single-purpose bot built to execute "
            "specific commands for your community. This service "
            "covers essential features such as custom text commands, "
            "automated response triggers, or basic utility tools. "
            "The bot will be delivered with clear setup instructions "
            "for your hosting environment.\n\n"
            "**Basic Setup — $2.50**\n"
            "**Common Setup — $3.75**\n"
            "**Advanced Setup — $5.00**"
        ),
    },

    "bot_upgrade": {
        "name": "Premium Bot Upgrades",
        "price": "$1.00 – $3.50 / Month",
        "details": (
            "Enhance your existing bots with advanced functionalities. "
            "This includes configuring multi-purpose automation, "
            "setting up complex interactive menus (buttons and "
            "dropdowns), or integrating API webhooks to stream live "
            "data, social media alerts, or business notifications "
            "directly into your channels."
        ),
    },

    "boosting": {
        "name": "Server Boosting Services",
        "price": "Coming Soon",
        "details": (
            "We will soon offer affordable server boosting packages "
            "to help elevate your community's status. Boosting your "
            "server will unlock premium perks, including higher audio "
            "quality, expanded emoji slots, a custom server banner, "
            "and increased upload limits for all members.\n\n"
            "**Stay tuned for launch dates and promotional bundle offers.**"
        ),
    },

    "starter_bundle": {
        "name": "Starter Community Bundle",
        "price": "$2.00",
        "details": (
            "Perfect for creators or businesses launching their first "
            "online space. This package combines our Base Server "
            "Creation with a Basic Custom Bot.\n\n"
            "You receive a fully structured server with essential "
            "role permissions, plus a dedicated bot configured with "
            "custom commands to engage your early members."
        ),
    },

    "growth_bundle": {
        "name": "Premium Growth Bundle",
        "price": "$5.00",
        "details": (
            "Designed for businesses looking to scale and automate "
            "their operations. This bundle includes our Advanced "
            "Server Setup, a Custom Bot, and Premium Feature Add-ons.\n\n"
            "We will build out advanced channels, self-assignable "
            "reaction roles, interactive button menus, and live "
            "API webhook notifications."
        ),
    },

    "ultimate_bundle": {
        "name": 'The "Ultimate Launch" Package',
        "price": "$8.25 — Coming Soon",
        "details": (
            "Our complete, all-in-one operational setup. This future "
            "tier will include everything from the Premium Growth "
            "Bundle, plus an introductory Server Boosting Package "
            "once our boosting services officially launch.\n\n"
            "This ensures your community looks established, runs "
            "automatically, and immediately benefits from higher "
            "audio and video quality."
        ),
    },
}


# ============================================================
# MAIN ORDER VIEW
# ============================================================

class OrderView(discord.ui.LayoutView):

    def __init__(self):
        super().__init__(timeout=300)

        self.selected_service = None
        self.build_panel()

    def build_panel(self):

        self.clear_items()

        selected_text = (
            f"**Selected:** {SERVICES[self.selected_service]['name']}"
            if self.selected_service
            else "**Selected:** None"
        )

        container = discord.ui.Container(

            discord.ui.TextDisplay(
                "# Nexus United\n"
                "## Service Catalog\n\n"
                "Choose a service or bundle to view its details "
                "and start an order."
            ),

            discord.ui.Separator(),

            discord.ui.TextDisplay(
                "## Services\n\n"

                "**Discord Server Creation**\n"
                "**Price:** $1.50 (Base Server) • "
                "$5.00–$10.00 (Advanced Setup)\n"
                "A fully structured server tailored to your "
                "community or business niche.\n\n"

                "**Custom Discord Bot**\n"
                "**Prices:** $2.50 (Basic) • $3.75 (Common) • "
                "$5.00 (Advanced)\n"
                "A dedicated, single-purpose bot built to execute "
                "specific commands for your community.\n\n"

                "**Premium Bot Upgrades**\n"
                "**Price:** $1.00–$3.50 / Month\n"
                "Enhance your existing bots with advanced "
                "functionalities.\n\n"

                "**Server Boosting Services**\n"
                "**Price:** Coming Soon\n"
                "Affordable server boosting packages coming soon."
            ),

            discord.ui.Separator(),

            discord.ui.TextDisplay(
                "## Service Bundles\n\n"

                '**Starter Community Bundle**\n'
                "**Price:** $2.00\n"
                "Base Server Creation + Basic Custom Bot.\n\n"

                "**Premium Growth Bundle**\n"
                "**Price:** $5.00\n"
                "Advanced Server Setup + Custom Bot + "
                "Premium Feature Add-ons.\n\n"

                '**The "Ultimate Launch" Package**\n'
                "**Price:** $8.25 (Coming Soon)\n"
                "Complete all-in-one operational setup."
            ),

            discord.ui.Separator(),

            discord.ui.TextDisplay(
                selected_text
            ),

            discord.ui.ActionRow(
                discord.ui.StringSelect(
                    placeholder="Select a service or bundle",
                    custom_id="order_service_select",
                    options=[
                        discord.SelectOption(
                            label="Discord Server Creation",
                            description="$1.50 Base • $5.00–$10.00 Advanced",
                            value="discord_server"
                        ),
                        discord.SelectOption(
                            label="Custom Discord Bot",
                            description="$2.50 Basic • $3.75 Common • $5 Advanced",
                            value="custom_bot"
                        ),
                        discord.SelectOption(
                            label="Premium Bot Upgrades",
                            description="$1.00–$3.50 / Month",
                            value="bot_upgrade"
                        ),
                        discord.SelectOption(
                            label="Server Boosting Services",
                            description="Coming Soon",
                            value="boosting"
                        ),
                        discord.SelectOption(
                            label="Starter Community Bundle",
                            description="$2.00",
                            value="starter_bundle"
                        ),
                        discord.SelectOption(
                            label="Premium Growth Bundle",
                            description="$5.00",
                            value="growth_bundle"
                        ),
                        discord.SelectOption(
                            label='The "Ultimate Launch" Package',
                            description="$8.25 — Coming Soon",
                            value="ultimate_bundle"
                        ),
                    ]
                )
            ),

            discord.ui.Separator(),

            discord.ui.ActionRow(
                discord.ui.Button(
                    label="View Details",
                    style=discord.ButtonStyle.primary,
                    custom_id="order_details"
                ),
                discord.ui.Button(
                    label="Start Order",
                    style=discord.ButtonStyle.success,
                    custom_id="order_start"
                ),
                discord.ui.Button(
                    label="Cancel",
                    style=discord.ButtonStyle.danger,
                    custom_id="order_cancel"
                )
            ),

            discord.ui.TextDisplay(
                "Select an item above, then choose an action."
            ),
        )

        self.add_item(container)

    async def interaction_check(
        self,
        interaction: discord.Interaction
    ) -> bool:

        custom_id = interaction.data.get("custom_id")

        if custom_id == "order_service_select":

            values = interaction.data.get("values", [])

            if values:
                self.selected_service = values[0]
                self.build_panel()

                await interaction.response.edit_message(
                    view=self
                )

            return False

        if custom_id == "order_details":

            if not self.selected_service:
                await interaction.response.send_message(
                    "Please select a service or bundle first.",
                    ephemeral=True
                )
                return False

            service = SERVICES[self.selected_service]

            await interaction.response.edit_message(
                view=ServiceDetailsView(
                    service_name=service["name"],
                    price=service["price"],
                    details=service["details"]
                )
            )

            return False

        if custom_id == "order_start":

            if not self.selected_service:
                await interaction.response.send_message(
                    "Please select a service or bundle first.",
                    ephemeral=True
                )
                return False

            service = SERVICES[self.selected_service]

            await interaction.response.edit_message(
                view=OrderRequirementsView(
                    service_name=service["name"]
                )
            )

            return False

        if custom_id == "order_cancel":

            await interaction.response.edit_message(
                view=CancelledView()
            )

            return False

        return True


# ============================================================
# SERVICE DETAILS VIEW
# ============================================================

class ServiceDetailsView(discord.ui.LayoutView):

    def __init__(
        self,
        service_name: str,
        price: str,
        details: str
    ):
        super().__init__(timeout=300)

        container = discord.ui.Container(

            discord.ui.TextDisplay(
                f"# {service_name}\n\n"
                f"**Price:** {price}"
            ),

            discord.ui.Separator(),

            discord.ui.TextDisplay(
                details
            ),

            discord.ui.Separator(),

            discord.ui.ActionRow(
                discord.ui.Button(
                    label="Start Order",
                    style=discord.ButtonStyle.success,
                    custom_id="details_start"
                ),
                discord.ui.Button(
                    label="Back to Catalog",
                    style=discord.ButtonStyle.secondary,
                    custom_id="details_back"
                )
            ),
        )

        self.add_item(container)

    async def interaction_check(
        self,
        interaction: discord.Interaction
    ) -> bool:

        custom_id = interaction.data.get("custom_id")

        if custom_id == "details_start":

            await interaction.response.edit_message(
                view=OrderRequirementsView(
                    service_name="Selected Service"
                )
            )

            return False

        if custom_id == "details_back":

            await interaction.response.edit_message(
                view=OrderView()
            )

            return False

        return True


# ============================================================
# ORDER REQUIREMENTS VIEW
# ============================================================

class OrderRequirementsView(discord.ui.LayoutView):

    def __init__(self, service_name: str):
        super().__init__(timeout=300)

        container = discord.ui.Container(

            discord.ui.TextDisplay(
                "# Create Order\n"
                "## Requirements\n\n"
                f"**Service:** {service_name}\n\n"
                "The order form will collect the information "
                "needed to complete your order."
            ),

            discord.ui.Separator(),

            discord.ui.TextDisplay(
                "### Order Information\n\n"
                "You will be asked for:\n"
                "• Your requirements\n"
                "• Preferred package\n"
                "• Additional details\n"
                "• Payment method"
            ),

            discord.ui.Separator(),

            discord.ui.ActionRow(
                discord.ui.Button(
                    label="Continue",
                    style=discord.ButtonStyle.success,
                    custom_id="requirements_continue"
                ),
                discord.ui.Button(
                    label="Cancel",
                    style=discord.ButtonStyle.danger,
                    custom_id="requirements_cancel"
                )
            ),
        )

        self.add_item(container)

    async def interaction_check(
        self,
        interaction: discord.Interaction
    ) -> bool:

        custom_id = interaction.data.get("custom_id")

        if custom_id == "requirements_continue":

            await interaction.response.send_message(
                "The order form will be added next.",
                ephemeral=True
            )

            return False

        if custom_id == "requirements_cancel":

            await interaction.response.edit_message(
                view=CancelledView()
            )

            return False

        return True


# ============================================================
# CANCELLED VIEW
# ============================================================

class CancelledView(discord.ui.LayoutView):

    def __init__(self):
        super().__init__(timeout=60)

        container = discord.ui.Container(
            discord.ui.TextDisplay(
                "# Order Cancelled\n\n"
                "Your order process has been cancelled.\n\n"
                "You can use `/order` whenever you're ready "
                "to start a new order."
            )
        )

        self.add_item(container)


# ============================================================
# COG
# ============================================================

class Order(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="order",
        description="Start a Nexus United service order."
    )
    async def order(
        self,
        interaction: discord.Interaction
    ):
        await interaction.response.send_message(
            view=OrderView()
        )


# ============================================================
# SETUP
# ============================================================

async def setup(bot: commands.Bot):
    await bot.add_cog(Order(bot))
