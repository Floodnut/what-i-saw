interface Invoice {
  customer: string;
  performances: Performance[];
}

interface Performance {
  playId: string;
  audience: number;
}

/**
 * ============================================================
 * ======================== 리팩터링 전 ==========================
 * ============================================================
 */
function statement(invoice: Invoice, plays: any): string {
  let totalAmount = 0;
  let volumeCredits = 0;
  let result = `청구 내역 (고객명: ${invoice.customer})\n`; // 개행문자 진짜 맘에 안듦.

  const format = new Intl.NumberFormat("en-US", {
    style: "currency",
    currency: "USD",
    minimumFractionDigits: 2,
  }).format;

  for (let perf of invoice.performances) {
    const play = plays[perf.playId];
    let thisAmount = 0;

    // 이 switch-case 메서드 화해서 map으로 뺀다면 어떨까?
    switch (play.type) {
      case "tragedy":
        thisAmount = 40000;
        if (perf.audience > 10) {
          thisAmount += 1000 * (perf.audience - 10);
        }
        break;
      case "comedy":
        thisAmount = 30000;
        if (perf.audience > 20) {
          thisAmount += 10000 + 500 * (perf.audience - 10);
        }
        thisAmount += 300 * perf.audience;
        break;
      default:
        throw new Error(`${play.type}`);
    }

    volumeCredits += Math.max(perf.audience - 30, 0);
    if ("comedy" === play.type) volumeCredits += Math.floor(perf.audience / 5);

    result += `${play.name}: ${format(thisAmount / 100)}`;
    result += `(${perf.audience}석)\n`;

    totalAmount += thisAmount;
  }

  result += `총액: ${format(totalAmount / 100)}\n`;
  result += `적립 포인트: ${volumeCredits}점\n`;

  return result; // 과연 result를 문자열로 리턴하는게 맞는가?
}

/**
 * ============================================================
 * ======================== 리팩터링 1 ==========================
 * ============================================================
 */

function statement_1(invoice: Invoice, plays: any): string {
  let totalAmount = 0;
  let volumeCredits = 0;
  let result = `청구 내역 (고객명: ${invoice.customer})\n`; // 개행문자 진짜 맘에 안듦.

  const format = new Intl.NumberFormat("en-US", {
    style: "currency",
    currency: "USD",
    minimumFractionDigits: 2,
  }).format;

  for (let perf of invoice.performances) {
    const play = plays[perf.playId];
    let thisAmount = calculateAmount(play, perf);

    // 이미 calculateAmount에서 play.type을 체크하고 있다.
    // 이걸 재활용 해볼 수 있을 것 같다.
    volumeCredits += Math.max(perf.audience - 30, 0);
    if ("comedy" === play.type) volumeCredits += Math.floor(perf.audience / 5);

    result += `${play.name}: ${format(thisAmount / 100)}`;
    result += `(${perf.audience}석)\n`;

    totalAmount += thisAmount;
  }

  result += `총액: ${format(totalAmount / 100)}\n`;
  result += `적립 포인트: ${volumeCredits}점\n`;

  return result; // 과연 result를 문자열로 리턴하는게 맞는가?
}

function calculateAmount(play: any, perf: Performance): number {
  let thisAmount = 0;

  switch (play.type) {
    case "tragedy":
      thisAmount = 40000;
      if (perf.audience > 10) {
        thisAmount += 1000 * (perf.audience - 10);
      }
      break;
    case "comedy":
      thisAmount = 30000;
      if (perf.audience > 20) {
        thisAmount += 10000 + 500 * (perf.audience - 10);
      }
      thisAmount += 300 * perf.audience;
      break;
    default:
      throw new Error(`${play.type}`);
  }

  return thisAmount;
}
