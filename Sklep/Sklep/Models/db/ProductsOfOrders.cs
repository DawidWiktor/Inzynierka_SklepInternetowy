
//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated from a template.
//
//     Manual changes to this file may cause unexpected behavior in your application.
//     Manual changes to this file will be overwritten if the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------


namespace Sklep.Models.db
{

using System;
    using System.Collections.Generic;
    
public partial class ProductsOfOrders
{

    public int ProductOfOrder { get; set; }

    public int ProductID { get; set; }

    public int NumOfOrderID { get; set; }

    public decimal Vat { get; set; }

    public int Quantity { get; set; }

    public decimal PriceN { get; set; }



    public virtual Orders Orders { get; set; }

    public virtual Products Products { get; set; }

}

}
