
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
    
public partial class Users
{

    [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA2214:DoNotCallOverridableMethodsInConstructors")]
    public Users()
    {

        this.Comments = new HashSet<Comments>();

        this.Orders = new HashSet<Orders>();

        this.Orders1 = new HashSet<Orders>();

    }


    public int UserID { get; set; }

    public string UserName { get; set; }

    public string Password { get; set; }

    public string Email { get; set; }

    public string Name { get; set; }

    public string Surname { get; set; }

    public string Link { get; set; }

    public string Street { get; set; }

    public string NumOfHouse { get; set; }

    public string PostCode { get; set; }

    public string City { get; set; }

    public string Role { get; set; }

    public Nullable<int> PhoneNumber { get; set; }

    public string IsActive { get; set; }



    [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA2227:CollectionPropertiesShouldBeReadOnly")]

    public virtual ICollection<Comments> Comments { get; set; }

    [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA2227:CollectionPropertiesShouldBeReadOnly")]

    public virtual ICollection<Orders> Orders { get; set; }

    [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA2227:CollectionPropertiesShouldBeReadOnly")]

    public virtual ICollection<Orders> Orders1 { get; set; }

}

}