# creates a nested dictionary of genes each with control and treatment values
expression_data = {}
expression_data["Gene 1"] = {}
expression_data["Gene 2"] = {}
expression_data["Gene 3"] = {}
expression_data["Gene 1"]["Control values"] = [10.5, 11.2, 10.8]
expression_data["Gene 1"]["Treatment values"] = [25.3, 24.7, 26.1]
expression_data["Gene 2"]["Control values"] = [8.2, 8.5, 8.0]
expression_data["Gene 2"]["Treatment values"] = [12.1, 11.8, 12.5]
expression_data["Gene 3"]["Control values"] = [15.0, 14.8, 15.2]
expression_data["Gene 3"]["Treatment values"] = [18.5, 18.2, 18.8]

# iterates through each gene in dictionary, calculating the mean of the control values and treatment values and the fold change
# and then prints results including information on if fold change is significant
for gene in expression_data:
    control_mean = sum(expression_data[gene]["Control values"])/len(expression_data[gene]["Control values"])
    treatment_mean = sum(expression_data[gene]["Treatment values"])/len(expression_data[gene]["Treatment values"])
    fold_change = treatment_mean/control_mean
    print(f"{gene} has mean expression of {control_mean:.2f} for control and {treatment_mean:.2f} for treatment.")
    if fold_change > 2.0 or fold_change < 0.5:
        print(f"{gene} has fold change of {fold_change:.2f}, which is significant.")
    else:
        print(f"{gene} has fold change of {fold_change:.2f}, which is not significant.")