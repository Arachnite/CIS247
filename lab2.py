
# Brandon Jun
# Lab #2

# Concert Ticket Sold
concert_name = "Summer Music Festival"
vip_tickets_sold = 25
general_tickets_sold = 150

# Ticket Prices
vip_ticket_price = 100
general_ticket_price = 50

# Gross Revenue
vip_revenue = vip_tickets_sold * vip_ticket_price
general_revenue = general_tickets_sold * general_ticket_price
gross_total = vip_revenue + general_revenue

# Profit Distribution
venue_percentage = 0.30
artist_percentage = 0.70

venue_profit = gross_total * venue_percentage
artist_profit = gross_total * artist_percentage

# Display Results
print("=== CONCERT SALES REPORT ===")
print(f"Concert Name:                    {concert_name}")
print(f"VIP Tickets Sold:                {vip_tickets_sold}")
print(f"General Admission Tickets Sold:  {general_tickets_sold}")
print()
print("=== REVENUE BREAKDOWN ===")
print(f"VIP Revenue:                     ${vip_revenue:,.2f}")
print(f"General Admission Revenue:       ${general_revenue:,.2f}")
print(f"Gross Total:                     ${gross_total:,.2f}")
print()
print("=== PROFIT DISTRIBUTION ===")
print(f"Venue Profit (30%):              ${venue_profit:,.2f}")
print(f"Artist Profit (70%):             ${artist_profit:,.2f}")
print()
print(f"Total Distributed:               ${venue_profit + artist_profit:,.2f}")