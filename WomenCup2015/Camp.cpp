#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Tnode {
  int L, R;
  vector<int> ids;
  Tnode* parent;

  Tnode (int l, int r, bool* rem) : parent(0) {
    for (int i=l; i<=r; ++i) {
      if (!rem[i]) {
        rem[i] = true;
        ids.push_back(i);
      }
    }
    if (!ids.empty()) {
      L = ids.front();
      R = ids.back();
    }
  }

  bool contains(int x) {
    if (x<L or x>R) return false;
    for (unsigned int i=0; i<=ids.size(); ++i) {
      if (x == ids[i]) return true;
    }
    return false;
  }
};

int main() {
  int N,M;
  int l,r;
  cin >> N >> M;
  bool rem[N+1] = {false};
  vector<Tnode*> circles;
  int c_size = 0;
  Tnode* nod;

  while (M--) {
    cin >> l >> r;
    Tnode* tmp = new Tnode(l,r,rem);
    //ignore empty circles
    if (tmp->ids.empty()) {
      delete(tmp);
      continue;
    }
    //add link parent-child
    for (int i=0; i<c_size; ++i) {
      nod = circles[i];
      if (l <= nod->L && r >= nod->R) {
        if (!nod->parent || l>nod->parent->L)
          nod->parent = tmp;
      }
      else if (l >= nod->L && r <= nod->R) {
        if (!tmp->parent || tmp->parent->L < nod->parent->L)
          tmp->parent = nod;
      }
    }
    circles.push_back(tmp);
    c_size++;
  }

  vector< pair<int,int> > links;
  for (int i=0; i<c_size; ++i) {
    nod = circles[i];
    Tnode* par = nod->parent;
    if (par) {
      if (par->contains(nod->L-1))
        links.push_back(make_pair(nod->L-1, nod->L));
      if (par->contains(nod->R+1))
        links.push_back(make_pair(nod->R, nod->R+1));
    }
  }

  sort(links.begin(), links.end());
  cout << links.size() << endl;
  for (unsigned int i=0; i<links.size(); ++i) {
    cout << links[i].first << " " << links[i].second << endl;
  }

  for (int i=0; i<c_size; ++i) {
    nod = circles[i];
    //cout << "L = " << nod->L << ", R = " << nod->R << endl;
    /*
    cout << "this = " << nod->L << "-" << nod->R;
    if (nod->parent)
      cout << "; parent = " << nod->parent->L << "-" << nod->parent->R;
    cout << endl;
    */
    delete(nod);
  }
}
