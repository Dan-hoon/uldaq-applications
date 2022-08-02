package com.dxc.Entities;

public class Employee {
    private String employee_id;
    private String employeeName;
    
    public Employee(String e, String f)
    {
        employee_id = e;
        employeeName = f;
    }

    public void setemployee_id(String s)
    {
        employee_id = s;
    }
    public void setemployee_name(String j)
    {
        employeeName = j;
    }

    public String getemployee_id()
    {
        return employee_id;
    }

    public String getemployee_name()
    {
        return employeeName;
    }

   
}