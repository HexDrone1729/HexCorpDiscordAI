import assign
import discord
import join
import sys

bot = discord.ext.commands.Bot('')

# register Cogs
bot.add_cog(join.Join(bot))
bot.add_cog(assign.Assign(bot))

bot.run(sys.argv[1])