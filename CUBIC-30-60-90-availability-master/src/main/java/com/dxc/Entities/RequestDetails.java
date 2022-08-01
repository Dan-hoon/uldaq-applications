package com.dxc.Entities;

//FILE NOT NEEDED.
public class RequestDetails {
    private String skill;
    private String jobTitle;
    private int jobLevel;
    private String ppm_roll_off;

    public void setSkill(String s)
    {
        skill = s;
    }
    public void setJobTitle(String j)
    {
        jobTitle = j;
    }

    public void setJobLevel(int l)
    {
        jobLevel = l;
    }

    public void setPpmRollOff(String roll_off)
    {
        ppm_roll_off = roll_off;
    }

    public String getSkill()
    {
        return skill;
    }

    public String getJobTitle()
    {
        return jobTitle;
    }

    public int getJobLevel()
    {
        return jobLevel;
    }

    public String getPpmRollOf()
    {
        return ppm_roll_off;
    }
    
}