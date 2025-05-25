class Var:
    def __init__(self, n): self.n = n
    def __repr__(self): return self.n
    def sub(self, θ): return θ.get(self.n, self)

class Const:
    def __init__(self, n): self.n = n
    def __repr__(self): return self.n
    def sub(self, θ): return self

class Pred:
    def __init__(self, nm, args): self.nm, self.args = nm, args
    def __repr__(self): return f"{self.nm}({', '.join(map(str,self.args))})"
    def sub(self, θ): return Pred(self.nm, [a.sub(θ) for a in self.args])

class Rule:
    def __init__(self, ants, cons): self.ants, self.cons = ants, cons
    def __repr__(self):
        return (" & ".join(map(str,self.ants))+"=>"+str(self.cons)) if self.ants else f"F:{self.cons}"
    def std(self):
        global _cnt
        _cnt+=1
        mp={}
        def rename(x):
            if isinstance(x,Var):
                mp.setdefault(x.n, Var(f"{x.n}_{_cnt}"))
                return mp[x.n]
            if isinstance(x,Pred):
                return Pred(x.nm, [rename(a) for a in x.args])
            return x
        return Rule([rename(a) for a in self.ants], rename(self.cons))

_cnt = 0

def unify(x, y, θ):
    if θ is None: return
    if x==y: return θ
    if isinstance(x,Var):
        if x.n in θ: return unify(θ[x.n], y, θ)
        if occurs(x,y,θ): return
        return {**θ, x.n:y}
    if isinstance(y,Var): return unify(y, x, θ)
    if type(x)!=type(y): return
    if isinstance(x,Const): return θ if x.n==y.n else
    if isinstance(x,Pred):
        if x.nm!=y.nm or len(x.args)!=len(y.args): return
        for a,b in zip(x.args,y.args):
            θ = unify(a.sub(θ), b.sub(θ), θ)
            if θ is None: return
        return θ

def occurs(v, x, θ):
    x = x.sub(θ)
    if v==x: return True
    if isinstance(x,Pred):
        return any(occurs(v,a,θ) for a in x.args)
    return False

def bc_or(kb, g, θ):
    for r in kb:
        r2 = r.std()
        θ2 = unify(r2.cons, g, θ)
        if θ2 is not None:
            if not r2.ants:
                yield θ2
            else:
                yield from bc_and(kb, [a.sub(θ2) for a in r2.ants], θ2)

def bc_and(kb, goals, θ):
    if not goals:
        yield θ; return
    first, rest = goals[0], goals[1:]
    for θ1 in bc_or(kb, first, θ):
        yield from bc_and(kb, rest, θ1)

def backward_chain(kb, query):
    yield from bc_or(kb, query, {})

if __name__=="__main__":
    john, mary, susan = Const('john'), Const('mary'), Const('susan')
    X, Y, Z = Var('X'), Var('Y'), Var('Z')
    kb = [
        Rule([], Pred('parent',[john,mary])),
        Rule([], Pred('parent',[mary,susan])),
        Rule([Pred('parent',[X,Y])], Pred('ancestor',[X,Y])),
        Rule([Pred('parent',[X,Z]), Pred('ancestor',[Z,Y])], Pred('ancestor',[X,Y]))
    ]
    q = Pred('ancestor',[john,susan])
    print("Query:", q)
    sols = list(backward_chain(kb, q))
    print("No solutions" if not sols else sols)
