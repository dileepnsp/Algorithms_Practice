def priceCheck(products, productPrices, productSold, soldPrice):
    # Write your code here
    p_dict={}
    errors=0
    for i,j in zip(products,productPrices):
        p_dict[i]=j
    print(p_dict)
    for i,j in zip(productSold,soldPrice):
        print(i,j)
        if p_dict[i] != j:
            errors+=1
    return errors

print(priceCheck(['eggs','milk','cheese'],[2.89,3.29,5.79],['eggs','eggs','cheese','milk'],[2.89,2.99,5.97,3.29]))