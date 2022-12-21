using System;

namespace ProgChallenge
{
  class SavingsAcct : Account
  {

    decimal _interest;
    int _count;

    public SavingsAcct(string fname, string lname, decimal interest, decimal balance = 0) : base(fname, lname, balance) {
      _interest = interest;
      _count = 0;
    }

    public override void Withdraw(decimal amount)
    {
      _count++;
      if (_count > 3)  {
        Console.WriteLine("More than 3 withdrawals - extra charge");
        amount += 2;
      }
      if (_balance - amount < 0) {
        Console.WriteLine("Attempt to overdraw savings - denied");
        return;
      }
      _balance -= amount;
    }

    public void ApplyInterest() {
      _balance += _balance * _interest;
    }
  }
}