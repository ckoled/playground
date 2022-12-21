using System;

namespace ProgChallenge
{
  class Account
  {
    protected string _fname;
    protected string _lname;
    protected decimal _balance;

    public Account(string fname, string lname, decimal balance=0) {
      _fname = fname;
      _lname = lname;
      _balance = balance;
    }

    public virtual void Deposit(decimal amount) {
      _balance += amount;
    }

    public virtual void Withdraw(decimal amount) {
      _balance -= amount;
    }

    public decimal Balance => _balance;

    public virtual string AccountOwner => $"{_fname} {_lname}";
  }
}