import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def calculate_tax(gross_income):
    standard_deduction = 75000
    taxable_income = max(0, gross_income - standard_deduction)

    def get_base_tax(income):
        tax = 0
        if income > 1500000:
            tax += (income - 1500000) * 0.30 + 150000
        elif income > 1200000:
            tax += (income - 1200000) * 0.20 + 90000
        elif income > 1000000:
            tax += (income - 1000000) * 0.15 + 60000
        elif income > 700000:
            tax += (income - 700000) * 0.10 + 30000
        elif income > 300000:
            tax += (income - 300000) * 0.05 + 0
        return tax

    def get_surcharge(income, base_tax):
        if income > 20000000:
            return base_tax * 0.25
        elif income > 10000000:
            return base_tax * 0.15
        elif income > 5000000:
            return base_tax * 0.10
        else:
            return 0

    base_tax = get_base_tax(taxable_income)
    surcharge = get_surcharge(taxable_income, base_tax)
    tax_with_surcharge = base_tax + surcharge

    # Marginal relief calculations
    if taxable_income > 20000000:
        tax_at_checkpoint = get_base_tax(20000000)
        surcharge_at_checkpoint = tax_at_checkpoint * 0.15
        max_tax = tax_at_checkpoint + surcharge_at_checkpoint + (taxable_income - 20000000)
        tax_with_surcharge = min(tax_with_surcharge, max_tax)
    elif taxable_income > 10000000:
        tax_at_checkpoint = get_base_tax(10000000)
        surcharge_at_checkpoint = tax_at_checkpoint * 0.10
        max_tax = tax_at_checkpoint + surcharge_at_checkpoint + (taxable_income - 10000000)
        tax_with_surcharge = min(tax_with_surcharge, max_tax)
    elif taxable_income > 5000000:
        tax_at_checkpoint = get_base_tax(5000000)
        surcharge_at_checkpoint = 0
        max_tax = tax_at_checkpoint + surcharge_at_checkpoint + (taxable_income - 5000000)
        tax_with_surcharge = min(tax_with_surcharge, max_tax)

    cess = tax_with_surcharge * 0.04
    return tax_with_surcharge + cess

# Deductions
epf_yearly = 1800 * 12
pt_yearly = 300 * 12

data = []
for gross in range(5000000, 25000001, 500000):
    tax = calculate_tax(gross)
    net_annual = gross - tax - epf_yearly - pt_yearly
    net_monthly = net_annual / 12
    data.append({
        'Gross Annual (INR)': gross,
        'Net Monthly Take Home (INR)': net_monthly,
        'Total Annual Tax (INR)': tax
    })

df = pd.DataFrame(data)
df.to_csv('take_home_salary_regime.csv', index=False)

# Plotting
plt.figure(figsize=(12, 7))
plt.plot(df['Gross Annual (INR)'], df['Net Monthly Take Home (INR)'], marker='o', linestyle='-', color='#1f77b4', linewidth=2, markersize=6)

# Formatting axes
def format_crores(x, pos):
    return f'₹{x/10000000:.2f} Cr' if x >= 10000000 else f'₹{x/100000:.0f} L'

def format_lakhs(x, pos):
    return f'₹{x/100000:.2f} L'

plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(format_crores))
plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(format_lakhs))

plt.title('Post-Tax Monthly Take-Home Salary (New Tax Regime)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Gross Annual Income', fontsize=12)
plt.ylabel('Monthly Take-Home Salary', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=45)

# Annotate a few key points (e.g., 50L, 1Cr, 1.5Cr, 2Cr, 2.5Cr)
key_points = [5000000, 10000000, 15000000, 20000000, 25000000]
for index, row in df.iterrows():
    if row['Gross Annual (INR)'] in key_points:
        plt.annotate(f"₹{row['Net Monthly Take Home (INR)']/100000:.2f}L",
                     (row['Gross Annual (INR)'], row['Net Monthly Take Home (INR)']),
                     textcoords="offset points", xytext=(0,10), ha='center', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig('take_home_salary.png', dpi=300)
