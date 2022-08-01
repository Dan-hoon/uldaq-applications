package com.dxc.Entities;

public class Employee {
    private String employee_id;
    private String employee_name;
    private String ppmrollOff;

    public Employee(String e, String n, String p)
    {
        //s.employee_id, e.employee_name, e.job_title, e.job_level, a.ppm_roll_off, s.workers_skill
        employee_id = e;
        employee_name = n;
        ppmrollOff = p;

    }

    public void set_employee_id(String s)
    {
        employee_id = s;
    }
    public void set_employee_name(String j)
    {
        employee_name = j;
    }

    
    public void set_ppmrolloff(String t)
    {
        ppmrollOff = t;
    }


    public String get_employee_id()
    {
        return employee_id;
    }

    public String get_employee_name()
    {
        return employee_name;
    }

    public String get_ppmrolloff()
    {
        return ppmrollOff;
    }
}