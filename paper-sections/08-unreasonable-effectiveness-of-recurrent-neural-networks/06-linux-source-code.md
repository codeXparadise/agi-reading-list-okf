---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/08-unreasonable-effectiveness-of-recurrent-neural-networks.md
source: ../../papers/08-unreasonable-effectiveness-of-recurrent-neural-networks.md
paper_title: The Unreasonable Effectiveness of Recurrent Neural Networks
sequence: 8
section: Linux Source Code
section_role: other
section_index: 6
pages: []
topics: ["../../topics/recurrent-neural-networks.md"]
description: "I wanted to push structured data to its limit, so for the final challenge I decided to use code. In particular, I took all the source and header…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Linux Source Code

> Section 6 of 10 from [08 - The Unreasonable Effectiveness of Recurrent Neural Networks](../../papers/08-unreasonable-effectiveness-of-recurrent-neural-networks.md) · `other` · pages n/a

I wanted to push structured data to its limit, so for the final challenge I decided to use code. In particular, I took all the source and header files found in the [Linux repo on Github](https://github.com/torvalds/linux), concatenated all of them in a single giant file (474MB of C code) (I was originally going to train only on the kernel but that by itself is only ~16MB). Then I trained several as-large-as-fits-on-my-GPU 3-layer LSTMs over a period of a few days. These models have about 10 million parameters, which is still on the lower end for RNN models. The results are superfun:

```
/*
 * Increment the size file of the new incorrect UI_FILTER group information
 * of the size generatively.
 */
static int indicate_policy(void)
{
  int error;
  if (fd == MARN_EPT) {
    /*
     * The kernel blank will coeld it to userspace.
     */
    if (ss->segment < mem_total)
      unblock_graph_and_set_blocked();
    else
      ret = 1;
    goto bail;
  }
  segaddr = in_SB(in.addr);
  selector = seg / 16;
  setup_works = true;
  for (i = 0; i < blocks; i++) {
    seq = buf[i++];
    bpf = bd->bd.next + i * search;
    if (fd) {
      current = blocked;
    }
  }
  rw->name = "Getjbbregs";
  bprm_self_clearl(&iv->version);
  regs->new = blocks[(BPF_STATS << info->historidac)] | PFMR_CLOBATHINC_SECONDS << 12;
  return segtable;
}
```

The code looks really quite great overall. Of course, I don’t think it compiles but when you scroll through the generate code it feels very much like a giant C code base. Notice that the RNN peppers its code with comments here and there at random. It is also very good at making very few syntactic errors. For example, it uses strings properly, pointer notation, etc. It also opens and closes brackets `{[` correctly and learns to indent its code very well. A common error is that it can’t keep track of variable names: It often uses undefined variables (e.g. `rw` above), declares variables it never uses (e.g. `int error`), or returns non-existing variables. Lets see a few more examples. Here’s another snippet that shows a wider array of operations that the RNN learns:\
\
```\
/*\
 * If this error is set, we will need anything right after that BSD.\
 */\
static void action_new_function(struct s_stat_info *wb)\
{\
  unsigned long flags;\
  int lel_idx_bit = e->edd, *sys & ~((unsigned long) *FIRST_COMPAT);\
  buf[0] = 0xFFFFFFFF & (bit << 4);\
  min(inc, slist->bytes);\
  printk(KERN_WARNING "Memory allocated %02x/%02x, "\
    "original MLL instead\n"),\
    min(min(multi_run - s->len, max) * num_data_in),\
    frame_pos, sz + first_seg);\
  div_u64_w(val, inb_p);\
  spin_unlock(&disk->queue_lock);\
  mutex_unlock(&s->sock->mutex);\
  mutex_unlock(&func->mutex);\
  return disassemble(info->pending_bh);\
}\
\
static void num_serial_settings(struct tty_struct *tty)\
{\
  if (tty == tty)\
    disable_single_st_p(dev);\
  pci_disable_spool(port);\
  return 0;\
}\
\
static void do_command(struct seq_file *m, void *v)\
{\
  int column = 32 << (cmd[2] & 0x80);\
  if (state)\
    cmd = (int)(int_state ^ (in_8(&ch->ch_flags) & Cmd) ? 2 : 1);\
  else\
    seq = 1;\
  for (i = 0; i < 16; i++) {\
    if (k & (1 << 1))\
      pipe = (in_use & UMXTHREAD_UNCCA) +\
        ((count & 0x00000000fffffff8) & 0x000000f) << 8;\
    if (count == 0)\
      sub(pid, ppc_md.kexec_handle, 0x20000000);\
    pipe_set_bytes(i, 0);\
  }\
  /* Free our user pages pointer to place camera if all dash */\
  subsystem_info = &of_changes[PAGE_SIZE];\
  rek_controls(offset, idx, &soffset);\
  /* Now we want to deliberately put it to device */\
  control_check_polarity(&context, val, 0);\
  for (i = 0; i < COUNTER; i++)\
    seq_puts(s, "policy ");\
}\
```\
\
Notice that in the second function the model compares `tty == tty`, which is vacuously true. On the other hand, at least the variable `tty` exists in the scope this time! In the last function, notice that the code does not return anything, which happens to be correct since the function signature is `void`. However, the first two functions were also declared `void` and did return values. This is again a form of a common mistake due to long-term interactions.\
\
Sometimes the model decides that it’s time to sample a new file. This is usually a very amusing part: The model first recites the GNU license character by character, samples a few includes, generates some macros and then dives into the code:\
\
```\
/*\
 *  Copyright (c) 2006-2010, Intel Mobile Communications.  All rights reserved.\
 *\
 *   This program is free software; you can redistribute it and/or modify it\
 * under the terms of the GNU General Public License version 2 as published by\
 * the Free Software Foundation.\
 *\
 *        This program is distributed in the hope that it will be useful,\
 * but WITHOUT ANY WARRANTY; without even the implied warranty of\
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\
 *\
 *  GNU General Public License for more details.\
 *\
 *   You should have received a copy of the GNU General Public License\
 *    along with this program; if not, write to the Free Software Foundation,\
 *  Inc., 675 Mass Ave, Cambridge, MA 02139, USA.\
 */\
\
#include <linux/kexec.h>\
#include <linux/errno.h>\
#include <linux/io.h>\
#include <linux/platform_device.h>\
#include <linux/multi.h>\
#include <linux/ckevent.h>\
\
#include <asm/io.h>\
#include <asm/prom.h>\
#include <asm/e820.h>\
#include <asm/system_info.h>\
#include <asm/setew.h>\
#include <asm/pgproto.h>\
\
#define REG_PG    vesa_slot_addr_pack\
#define PFM_NOCOMP  AFSR(0, load)\
#define STACK_DDR(type)     (func)\
\
#define SWAP_ALLOCATE(nr)     (e)\
#define emulate_sigs()  arch_get_unaligned_child()\
#define access_rw(TST)  asm volatile("movd %%esp, %0, %3" : : "r" (0));   \\
  if (__type & DO_READ)\
\
static void stat_PC_SEC __read_mostly offsetof(struct seq_argsqueue, \\
          pC>[1]);\
\
static void\
os_prefix(unsigned long sys)\
{\
#ifdef CONFIG_PREEMPT\
  PUT_PARAM_RAID(2, sel) = get_state_state();\
  set_pid_sum((unsigned long)state, current_state_str(),\
           (unsigned long)-1->lr_full; low;\
}\
```\
\
There are too many fun parts to cover- I could probably write an entire blog post on just this part. I’ll cut it short for now, but here is [1MB of sampled Linux code](http://cs.stanford.edu/people/karpathy/char-rnn/linux.txt) for your viewing pleasure.\
\

---

Full document: [08 - The Unreasonable Effectiveness of Recurrent Neural Networks](../../papers/08-unreasonable-effectiveness-of-recurrent-neural-networks.md) · Page-level evidence: [paper-pages/08-unreasonable-effectiveness-of-recurrent-neural-networks](../../paper-pages/08-unreasonable-effectiveness-of-recurrent-neural-networks/index.md)
