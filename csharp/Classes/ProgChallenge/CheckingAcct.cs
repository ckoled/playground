using System;

namespace ProgChallenge
{
  class CheckingAcct : Account
  {
    public CheckingAcct(string fname, string lname, decimal balance = 0) : base(fname, lname, balance) {}

    public override void Withdraw(decimal amount)
    {
      if (_balance - amount < 0)
        amount += 35;
      _balance -= amount;
    }
  }
}