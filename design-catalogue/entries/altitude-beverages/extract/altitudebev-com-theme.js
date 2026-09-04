// React Theme — extracted from https://altitudebev.com
// Compatible with: Chakra UI, Stitches, Vanilla Extract, or any CSS-in-JS

/**
 * TypeScript type definition for this theme:
 *
 * interface Theme {
 *   colors: {
    background: string;
    foreground: string;
    neutral50: string;
    neutral100: string;
    neutral200: string;
    neutral300: string;
 *   };
 *   fonts: {
    mono: string;
    body: string;
 *   };
 *   fontSizes: {
    '11': string;
    '12': string;
    '14': string;
    '16': string;
    '18': string;
    '40': string;
    '60': string;
    '160': string;
    '11.2': string;
 *   };
 *   space: {
    '2': string;
    '36': string;
    '48': string;
    '56': string;
    '64': string;
    '78': string;
    '85': string;
    '96': string;
    '125': string;
    '265': string;
    '288': string;
    '320': string;
    '333': string;
    '495': string;
 *   };
 *   radii: {
    full: string;
 *   };
 *   shadows: {

 *   };
 *   states: {
 *     hover: { opacity: number };
 *     focus: { opacity: number };
 *     active: { opacity: number };
 *     disabled: { opacity: number };
 *   };
 * }
 */

export const theme = {
  "colors": {
    "background": "#808080",
    "foreground": "#000000",
    "neutral50": "#fafafa",
    "neutral100": "#000000",
    "neutral200": "#53606e",
    "neutral300": "#808080"
  },
  "fonts": {
    "mono": "'DepartureMono', monospace",
    "body": "'EditorialNew', sans-serif"
  },
  "fontSizes": {
    "11": "11px",
    "12": "12px",
    "14": "14px",
    "16": "16px",
    "18": "18px",
    "40": "40px",
    "60": "60px",
    "160": "160px",
    "11.2": "11.2px"
  },
  "space": {
    "2": "2px",
    "36": "36px",
    "48": "48px",
    "56": "56px",
    "64": "64px",
    "78": "78px",
    "85": "85px",
    "96": "96px",
    "125": "125px",
    "265": "265px",
    "288": "288px",
    "320": "320px",
    "333": "333px",
    "495": "495px"
  },
  "radii": {
    "full": "110px"
  },
  "shadows": {},
  "states": {
    "hover": {
      "opacity": 0.08
    },
    "focus": {
      "opacity": 0.12
    },
    "active": {
      "opacity": 0.16
    },
    "disabled": {
      "opacity": 0.38
    }
  }
};

// MUI v5 theme
export const muiTheme = {
  "palette": {
    "background": {
      "default": "#808080",
      "paper": "#000000"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#fafafa"
    }
  },
  "typography": {
    "fontFamily": "'HelveticaNowDisplay', sans-serif",
    "h1": {
      "fontSize": "40px",
      "fontWeight": "200",
      "lineHeight": "42.4px"
    },
    "body1": {
      "fontSize": "16px",
      "fontWeight": "400",
      "lineHeight": "24px"
    },
    "body2": {
      "fontSize": "14px",
      "fontWeight": "400",
      "lineHeight": "20px"
    }
  },
  "shape": {
    "borderRadius": 32
  },
  "shadows": []
};

export default theme;
